import json

def get_mock_characters():
    return [
        {
            "Full Name": "Victor Sterling",
            "Faction or Affiliation": "Information Club",
            "Physical Appearance": "Immaculately groomed, wearing a pristine white thermal suit that looks untouched by the harsh world outside. Sharp features with cold, calculated eyes.",
            "Traits and Personality": "Fanatical, obsessive, and highly articulate. He views the global freezing as a necessary purification and worships the meteor's anomalies as divine.",
            "Mindset and Motivation": "To hoard and decipher all knowledge regarding the Meteor/Evolution phenomenon, believing the Information Club will ascend as the new rulers of a frozen Earth.",
            "Powers or Special Abilities": "Cognitive processing enhancement: Can absorb and recall vast amounts of data instantly, and slightly influence the thoughts of those with weaker wills.",
            "Current Location": "Sector 7 Geo-Dome (A fully heated, well-lit underground sanctuary with abundant food and clean water, shielded from the -70°C cold).",
            "Items and Equipment Carried": "High-tier data pad, biometric security key, heated thermos with real coffee, concealed stun pistol.",
            "Background Notes and Additional Information": "Before the freeze, he was a mid-level data analyst. The meteor event triggered a psychological break, leading to his fanatical devotion to the Information Club."
        },
        {
            "Full Name": "Elena Rostova",
            "Faction or Affiliation": "Ash Scavengers",
            "Physical Appearance": "Gaunt and frostbitten, wrapped in multiple layers of mismatched, grimy rags. Her eyes are tired but fierce, and she has a prominent scar across her left cheek from a frost-walker encounter.",
            "Traits and Personality": "Pragmatic, cynical, and fiercely independent. She trusts no one but is extremely protective of her few remaining allies.",
            "Mindset and Motivation": "Day-to-day survival. Her only goal is to find enough fuel and scraps to survive another night in the relentless -70°C wasteland.",
            "Powers or Special Abilities": "Thermal resilience: A minor mutation that allows her body to naturally generate slightly more heat than a normal human, preventing immediate hypothermia.",
            "Current Location": "Ruins of the Old Subway System (A freezing, damp, and dark tunnel where temperatures still drop to lethal levels without a constant fire).",
            "Items and Equipment Carried": "Makeshift spear tipped with scrap metal, a half-empty lighter, a heavily patched wool blanket, two cans of expired beans.",
            "Background Notes and Additional Information": "She lost her family during the initial temperature plummet. She refuses to join major factions like the Information Club due to their cruelty towards outsiders."
        }
    ]

def sort_characters(character_list):
    """Sort the list of characters alphabetically by name."""
    return sorted(character_list, key=lambda x: x.get("Full Name", ""))

def export_to_markdown(character_list, filename="character_database.md"):
    """Export the list of characters to a formatted markdown file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Character Database\n\n")
        for character in character_list:
            f.write(f"## {character.get('Full Name', 'Unknown')}\n\n")
            for key, value in character.items():
                f.write(f"- **{key}:** {value}\n")
            f.write("\n")

if __name__ == "__main__":
    characters = get_mock_characters()
    sorted_characters = sort_characters(characters)
    export_to_markdown(sorted_characters)
    print("Character database exported successfully.")
