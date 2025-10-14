from utils.load import load_data
from visualiation.threed_animation import threed_animation

if __name__ == "__main__":
    mixed_demographics_df, all_samples = load_data("./data/training_data")
    threed_animation(all_samples[54])
    