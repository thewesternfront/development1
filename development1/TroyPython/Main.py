
def main():
    print("Testing Python")

    count = 10 ** 6
    nums = []
    for i in range(count):
        nums.append(i)
        #nums.insert(0,i)
    nums.reverse()

    for i in range(count):
        print(nums[i])



if __name__ == "__main__":
    main()
