# 1. Reusable function to assemble the final screenplay layout
def build_story_blueprint(protagonist, timeline, twist, tone_style):
    blueprint = f"""
    ==================================================
    🎬 HIGH-RPM OTT SCENARIO BLUEPRINT
    ==================================================
    👤 CHARACTER ARC : The story follows {protagonist}.
    ⏳ CHRONOLOGY    : Set during the era of {timeline}.
    🎭 PLOT TWIST    : The narrative pivots when {twist}.
    🎨 CINEMATOGRAPHY: Render scenes in a {tone_style} aesthetic.
    ==================================================
    """
    return blueprint

# 2. Main execution flow to gather single-hand text inputs
print("--- STARTING THE POLYMATH STORY DESIGN ENGINE ---")

hero = input("Enter your main character type (e.g., A rogue radar officer): ")
era = input("Enter the historical/future era (e.g., Peak of the Cold War, 1962): ")
climax = input("Enter the massive plot twist: ")
visual_style = input("Enter the visual art style (e.g., Dark 2D graphic novel): ")

# 3. Process inputs through the automation function
final_script_blueprint = build_story_blueprint(hero, era, climax, visual_style)

# 4. Output the ready-to-copy result to the terminal console
print(final_script_blueprint)
print("👉 Copy this output layout straight into Claude for full script generation.")
