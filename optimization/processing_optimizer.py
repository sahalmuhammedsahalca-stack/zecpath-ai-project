def calculate_processing_efficiency(
    processed_items,
    processing_time_seconds
):
    """
    Calculate processing efficiency based on items
    processed per second.
    """

    if processing_time_seconds <= 0:
        return {
            "items_processed": processed_items,
            "processing_time_seconds": processing_time_seconds,
            "items_per_second": 0,
            "status": "Invalid Processing Time"
        }

    items_per_second = (
        processed_items / processing_time_seconds
    )

    if items_per_second >= 10:
        status = "High Efficiency"

    elif items_per_second >= 5:
        status = "Moderate Efficiency"

    else:
        status = "Low Efficiency"

    return {
        "items_processed": processed_items,
        "processing_time_seconds": processing_time_seconds,
        "items_per_second": round(items_per_second, 2),
        "status": status
    }