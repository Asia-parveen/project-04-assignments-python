print("This is Mad libs Python Project")

# Mad Libs Game-Adventure & Fantasy Version!
# 🌟 Exciting Welcome Message

print("✨🎭 Welcome to the Ultimate Mad Libs Adventure! 🎭✨")
print("Get ready to unleash your creativity and craft a hilarious, fun-filled story! 🚀")
print("Fill in the blanks with your favorite words, and let's create a masterpiece together. 🎨📖")
print("🌟 Let the storytelling magic begin! ✍️✨\n")

story_template = """
On a {adjective1} afternoon, {name} decided to explore the {place}.
As they walked through the {adjective2} surroundings, they encountered a {animal}
that was {verb1} near a {object}.

Curious, {name} approached the {animal} and offered it some {food}. To their surprise,
the {animal} spoke and said, '{dialogue}' 😲. Excited by this magical encounter,
{name} started {verb2} with joy.

It was a day to remember! 🌟
"""

name = input("👤 Enter a name: ")
adjective1 = input("🎭 Enter an adjective (describing the day): ")
place = input("📍 Enter a place: ")
adjective2 = input("🎨 Enter an adjective (describing the surroundings): ")
animal = input("🐅 Enter an animal: ")
verb1 = input("⚡ Enter a verb (action word - past tense): ")
object = input("📦 Enter an object: ")
food = input("🍔 Enter a food item: ")
dialogue = input("💬 Enter a short phrase (what the animal says): ")
verb2 = input("🏃 Enter an action (something fun to do): ")

# 🎉 Generate the Story
final_story = story_template.format(
    name=name, adjective1=adjective1, place=place,
    adjective2=adjective2, animal=animal, verb1=verb1,
    object=object, food=food, dialogue=dialogue, verb2=verb2
)


print("\n✨ Your Customized Mad Libs Story ✨")
print(final_story)