num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if (update_direction == 3) else num_users - 1

print('New value is:', num_users)
