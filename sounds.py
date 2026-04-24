from pygame import mixer

def load_sounds(keys):
    mixer.init()
    sounds = {}
    for key, filename in keys.items():
        sounds[key] = mixer.Sound(f"assets/sounds/{filename}")
    return sounds
