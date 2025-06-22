import logging

logger = logging.getLogger(__name__)

async def embed_document(*args, **kwargs) -> None:
    """Placeholder embedding task."""
    logger.info("Running embed_document task", extra={"args": args, "kwargs": kwargs})

