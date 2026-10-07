"""Small policy-neutral reference module for executable acceptance checks.

The module receives policy choices such as ``grace_minutes`` as inputs. It
does not decide which product-policy value is correct.

It follows the contract style from the Week 6 lecture: preconditions are
checked with ``if`` and ``raise ValueError``, and the types say which values
are allowed.
"""

from typing import Literal

Disposition = Literal["active", "held", "releasable"]
"""The release state of a reservation at the checkout desk."""

DISPOSITIONS: tuple[Disposition, ...] = ("active", "held", "releasable")


def reservation_disposition(
    *,
    minutes_after_start: int,
    grace_minutes: int,
    checked_in: bool,
    staff_hold_until: int | None = None,
) -> Disposition:
    """Return the reservation state under an already configured policy.

    Call it with named arguments, for example:
    reservation_disposition(minutes_after_start=5, grace_minutes=10, checked_in=False)

    Preconditions, checked with ValueError:
    - minutes_after_start is zero or greater.
    - grace_minutes is zero or greater.
    - staff_hold_until, when given, is zero or greater. It is measured in
      minutes after the reservation start, like minutes_after_start.

    Postconditions:
    - A checked-in reservation is "active".
    - Before a recorded staff hold ends, the reservation is "held".
    - Before the configured grace period ends, the reservation is "held".
    - Otherwise the reservation is "releasable".
    """
    if minutes_after_start < 0:
        raise ValueError("minutes_after_start must be zero or greater")
    if grace_minutes < 0:
        raise ValueError("grace_minutes must be zero or greater")
    if staff_hold_until is not None and staff_hold_until < 0:
        raise ValueError("staff_hold_until must be zero or greater")

    if checked_in:
        return "active"

    if staff_hold_until is not None and minutes_after_start < staff_hold_until:
        return "held"

    if minutes_after_start < grace_minutes:
        return "held"

    return "releasable"


def can_offer_to_waitlist(
    *,
    disposition: Disposition,
    preparation_complete: bool,
) -> bool:
    """Return whether the equipment may be offered to the waitlist.

    Call it with named arguments, for example:
    can_offer_to_waitlist(disposition="releasable", preparation_complete=True)

    Precondition, checked with ValueError:
    - disposition is "active", "held", or "releasable".

    Postcondition:
    - Returns True only when the reservation is "releasable" and the
      equipment is physically ready for the next checkout. A release
      decision alone is not enough.
    """
    if disposition not in DISPOSITIONS:
        raise ValueError(f"unknown disposition: {disposition}")

    return disposition == "releasable" and preparation_complete
