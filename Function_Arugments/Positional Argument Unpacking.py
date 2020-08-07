from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
full_path = join(path_segment_1, path_segment_2, path_segment_3)
print(full_path)

def myjoin(*args):
  joined = ""
  for arg in args:
    joined += join(arg) + " "
  return joined

print(myjoin("Hi", "my", "name", "is"))