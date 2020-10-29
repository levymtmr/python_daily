data = ['read', 'profile:read_all', 'activity:read_all']
data_test = ['read', 'activity:read_all', 'profile:read_all']

print(set(data) == set(data_test))