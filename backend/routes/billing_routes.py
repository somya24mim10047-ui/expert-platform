from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

def process_bill(call_id: int, minutes: int):

    amount = minutes * 2

    print(
        f"Call {call_id} billed ₹{amount}"
    )

@router.post("/bill")
def bill_call(
    call_id: int,
    minutes: int,
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(
        process_bill,
        call_id,
        minutes
    )

    return {
        "message": "Billing started in background"
    }