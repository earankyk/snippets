import argparse
#import pyprofiler

def read_large_file(file):
    with open(file) as f:
        for line in f:
            yield line

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read a large file efficiently")
    parser.add_argument('filename', help='filename')
    args = parser.parse_args()
    #profiler = pyprofiler.start_profile()
    reader = read_large_file(args.filename)
    while True:
        try:
            print(next(reader))
        except StopIteration:
            break
    #pyprofiler.end_profile(profiler)
