from utilities.driver_setup import get_driver
from utilities.common_utils import take_screenshot


def before_all(context):
    print("🎯 Browser started once only")
    context.driver = get_driver()


def after_all(context):
    print("✅ Closing browser after all features complete")
    context.driver.quit()


def before_scenario(context, scenario):
    print(f"🚀 Starting scenario: {scenario.name}")


def after_scenario(context, scenario):
    print(f"✅ Completed scenario: {scenario.name}")


def after_step(context, step):
    if step.status == "failed":
        take_screenshot(context.driver, step.name)
