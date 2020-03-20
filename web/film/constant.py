class Active:
    deactivate = 0
    active = 1
    pending = 2
    rejected = 3

    FieldStr = \
        {
            deactivate: "Deactivate",
            active: "Active",
            pending: "Pending",
            rejected: "Rejected",
        }


class ActiveBool:
    deactivate = 0
    activate = 1

    FieldStr = {
        deactivate: "Deactivate",
        activate: "Activate"
    }

class Type:
    customer = 1
    staff = 2

    FieldStr = {
        customer:"Customer",
        staff:"Staff",
    }
