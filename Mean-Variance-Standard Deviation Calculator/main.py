import numpy as np

x = 1
values = []

while x < 10:
    try:
        value = int(input(f"Listenin {x}.elemanını giriniz: "))
        values.append(value)
        x+=1
    except ValueError as err:
        print("Lütfen sayısal bir değer giriniz! ")

array = np.array(values)

def calculate(array):
    flat = array
    array = array.reshape(3,3)

    def mean():
        row1_mean = array[0,:].mean()
        row2_mean = array[1,:].mean()
        row3_mean = array[2,:].mean()
        row_mean = [row1_mean,row2_mean,row3_mean]

        column1_mean = array[:,0].mean()
        column2_mean = array[:,1].mean()
        column3_mean = array[:,2].mean()
        column_mean = [column1_mean,column2_mean,column3_mean]

        flat_mean=flat.mean()

        mean_list = [column_mean,row_mean,flat_mean]
        return(mean_list)

    def variance():
        row1_variance=array[0,:].var()
        row2_variance=array[1,:].var()
        row3_variance=array[2,:].var()
        row_variance = [row1_variance,row2_variance,row3_variance]
        
        column1_variance=array[:,0].var()
        column2_variance=array[:,1].var()
        column3_variance=array[:,2].var()
        column_variance = [column1_variance,column2_variance,column3_variance]

        flat_variance=flat.var()

        variance_list = [column_variance,row_variance,flat_variance]
        return(variance_list)

    def std():
        row1_std=array[0,:].std()
        row2_std=array[1,:].std()
        row3_std=array[2,:].std()
        row_std = [row1_std,row2_std,row3_std]
        
        column1_std=array[:,0].std()
        column2_std=array[:,1].std()
        column3_std=array[:,2].std()
        column_std = [column1_std,column2_std,column3_std]

        flat_std=flat.std()

        std_list = [column_std,row_std,flat_std]
        return(std_list)

    def max():
        row1_max=array[0,:].max()
        row2_max=array[1,:].max()
        row3_max=array[2,:].max()
        row_max = [row1_max,row2_max,row3_max]
        
        column1_max=array[:,0].max()
        column2_max=array[:,1].max()
        column3_max=array[:,2].max()
        column_max = [column1_max,column2_max,column3_max]

        flat_max=flat.max()

        max_list = [column_max,row_max,flat_max]
        return(max_list)

    def min():
        row1_min=array[0,:].min()
        row2_min=array[1,:].min()
        row3_min=array[2,:].min()
        row_min = [row1_min,row2_min,row3_min]
        
        column1_min=array[:,0].min()
        column2_min=array[:,1].min()
        column3_min=array[:,2].min()
        column_min = [column1_min,column2_min,column3_min]

        flat_min=flat.min()

        min_list= [column_min,row_min,flat_min]
        return(min_list)

    def sum():
        row1_sum=array[0,:].sum()
        row2_sum=array[1,:].sum()
        row3_sum=array[2,:].sum()
        row_sum = [row1_sum,row2_sum,row3_sum]
        
        column1_sum=array[:,0].sum()
        column2_sum=array[:,1].sum()
        column3_sum=array[:,2].sum()
        column_sum = [column1_sum,column2_sum,column3_sum]

        flat_sum=flat.sum()

        sum_list= [column_sum,row_sum,flat_sum]
        return(sum_list)


    dic = {
    'mean': [mean()],
    'variance': [variance()],
    'standard deviation': [std()],
    'max': [max()],
    'min': [min()],
    'sum': [sum()]
    }

    return(dic)
 
print(calculate(array))

