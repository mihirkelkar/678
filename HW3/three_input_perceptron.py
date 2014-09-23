threshold = 0.5
learning_rate = 0.1
weights = [0, 0, 0]
training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]
 
 
def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))

counter = 0 
while counter < 1000000:
    print('-' * 60)
    for input_vector, desired_output in training_set:
        print(weights)
        result = dot_product(input_vector, weights) > threshold
        error = desired_output - result
        for index, value in enumerate(input_vector):
            weights[index] += learning_rate * error * value
    
    counter += 1
