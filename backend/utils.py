import logging

def configure_logging(level:str = "INFO"):
    """Configure global logging format and level."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )
