import numpy as np

def power_method(mat, start, maxit):
    a = mat

    x = start

    max_iteration = maxit

    # Power Method Implementation
    lambda_old = 1.0
    condition =  True
    step = 1
    while condition:
        # Multiplying a and x
        x = np.matmul(a,x)
        
        # Finding new Eigen value and Eigen vector
        lambda_new = max(abs(x))
        
        x = x/lambda_new
        
        # Displaying Eigen value and Eigen Vector
        print('\nSTEP %d' %(step))
        print('----------')
        print('Eigen Value = %0.4f' %(lambda_new))
        print('Eigen Vector: ')
        for i in range(len(a)):
            print('%0.3f\t' % (x[i]))
        
        # Checking maximum iteration
        step = step + 1
        if step > max_iteration:
            print('Not convergent in given maximum iteration!')
            break
        
        # Calculating error
        error = abs(lambda_new - lambda_old)
        print('errror='+ str(error))
        lambda_old = lambda_new

def power_method_about(mat, start, maxit, closest):
    a = mat

    x = start

    max_iteration = maxit

    # Power Method Implementation
    lambda_old = 1.0
    condition =  True
    step = 1
    while step > max_iteration:
        # Multiplying a and x
        e = closest*np.eye(np.shape(mat)[0])
        x = np.matmul(np.linalg.inv(a-e),x)
        
        # Finding new Eigen value and Eigen vector
        lambda_new = max(abs(x))
        
        x = x/lambda_new
        
        # Displaying Eigen value and Eigen Vector
        # print('\nSTEP %d' %(step))
        # print('----------')
        # print('Eigen Value = %0.4f' %(lambda_new))
        # print('Eigen Vector: ')
        # for i in range(len(a)):
        #     print('%0.3f\t' % (x[i]))
        
        # Checking maximum iteration
        step = step + 1
        
        # Calculating error
        # error = abs(lambda_new - lambda_old)
        # print('errror='+ str(error))
        # lambda_old = lambda_new

    return x