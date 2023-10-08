import pandas as pd

df1 = pd.read_csv('output.csv')
members = df1['number']


df = pd.DataFrame({'members': members})

input_sequences = []
outputs = []

# Create input sequences and outputs
for i in range(len(df) - 10):
    input_seq = df['members'][i:i + 10].tolist()  # Get the last 10 members as input
    output = df['members'][i + 10]  # Get the 11th member as output
    input_sequences.append(input_seq)
    outputs.append(output)

data = pd.DataFrame({'input_sequences': input_sequences, 'output': outputs})

print(data.head())

