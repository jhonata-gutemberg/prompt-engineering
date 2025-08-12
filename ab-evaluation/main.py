from openai import OpenAI
import os

promptA = """Product description: A pair of shoes that can fit any foot size.
Seed words: adaptable, fit, omni-fit.
Product names:"""

promptB = """Product description: A home milkshake maker.
Seed words: fast, healthy, compact.
Product names: HomeShaker, Fit Shaker, QuickShake, ShakeMaker

Product description: A watch that can tell accurate time in space.
Seed words: astronaut, space-hardened, eliptical orbit
Product names: AstroTime, SpaceGuard, Orbit-Accurate, EliptoTime.

Product description: A pair of shoes that can fit any footsize.
Seed words: adaptable, fit, omni-fit.
Product names:"""

testPrompts = [promptA, promptB]

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

print(client)
