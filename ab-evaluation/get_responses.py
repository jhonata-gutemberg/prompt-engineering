from openai import OpenAI
import os
import pandas

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
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
responses = []
numTests = 5

def getResponse(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

for idx, prompt in enumerate(testPrompts):
    variant = chr(ord('A') + idx)
    for i in range(numTests):
        response = getResponse(prompt)
        data = {
            "variant": variant,
            "prompt": prompt,
            "response": response
        }
        responses.append(data)
df = pandas.DataFrame(responses)
df.to_csv("responses.csv", index=False)