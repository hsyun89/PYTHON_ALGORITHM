#배열
dataset = ['mical','Mical','MMMical']

m_count = 0
for data in dataset:
    for idx in range(len(data)):
        if data[idx] == 'M':
            m_count += 1

print(m_count)


