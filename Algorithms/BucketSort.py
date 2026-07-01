from typing import List

def bucket_sort(arr) -> List:
    bucket_size = len(arr)
    bucket = []
    final = []

    # Create buckets
    for _ in range(bucket_size):
        bucket.append([])

    for i in arr:
        bucket_index = int(bucket_size * i)
        bucket[bucket_index].append(i)

    print("bucket before sorting: ", bucket)

    for b in bucket:
        b.sort()
        final += b

    print("final array: ", final)



if __name__ == "__main__":
    # input_array = [8,5,9,3,10]
    input_array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    bucket_sort(input_array)