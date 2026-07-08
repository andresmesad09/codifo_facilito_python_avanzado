import logging
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(funcName)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


async def worker(name, delay):
    logger.info(f"{name} Inicio")
    await asyncio.sleep(delay)
    logger.info(f"{name} Finalizada")


async def main():
    await asyncio.gather(
        worker("function_a", 1),
        worker("function_b", 2),
        worker("function_c", 3),
    )


if __name__ == "__main__":
    asyncio.run(main())
