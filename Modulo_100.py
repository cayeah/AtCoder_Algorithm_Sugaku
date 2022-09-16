int(input())

mod_list = []

mod_list = list(map(int, input().split()))
print(sum(mod_list) % 100)