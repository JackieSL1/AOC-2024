import sys

filename = sys.argv[1]
with open(filename) as f:
    input = f.read().rstrip()

def fragment_disk(disk: str) -> int:
    result = 0
    on_file = True
    out_of_space = False

    position = 0

    # Offset should start on first file
    if len(disk)%2==0:
        right_offset = -2
    else:
        right_offset = -1
    right_size = 0

    left_id = 0
    right_id = (len(disk) // 2) + 1

    for _, item in enumerate(disk):
        size = int(item)

        if on_file:
            # We're looking at a file
            for _ in range(size):

                if left_id >= right_id:
                    if right_size == 0:
                        break

                    right_size -= 1

                print(left_id, end="")
                result += position * left_id
                position += 1

            # The next item will be free space
            on_file = False
            left_id += 1

            if out_of_space:
                break

        else:
            # We're looking at free space
            for _ in range(size):
                if left_id >= right_id:
                    out_of_space = True

                if right_size == 0:
                    if out_of_space:
                        break

                    right_id -= 1
                    right_size = int(disk[right_offset])
                    right_offset -= 2

                print(right_id, end="")
                result += position * right_id
                position += 1
                right_size -= 1

            # The next item will be a file
            on_file = True
            if out_of_space:
                for _ in range(right_size):
                    result += position * left_id
                    print(left_id, end="")
                    position += 1
                break


    return result

print(f"\n{fragment_disk(input)=}")
