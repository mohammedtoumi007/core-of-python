# ******* Math & Statistics *******


###Averages and measures of central location###

# ******* mean(): Arithmetic mean ("average") of data *******
import statistics as st
st.mean([1,2,3,4])

# ******* harmonic(): Harmonic meanv of data *******
st.harmonic_mean([2.5,3,10])

# ******* median(): Median (middle value) of data *******
st.median([1,3,5,7])

# ******* median_low(): Low median of data *******
st.median_low([1,3,5])

# ******* median_high(): High median of data *******
st.median_high([1,3,5,7])

# ******* median_grouped(): Median, or 50th percentile, of grouped data *******
st.median_grouped([52,52,53,54])

# ******* mode(): Mode (most common value) of discrete data *******
st.mode([1,1,3,3,3,3,4])

###Measures of spread###

# ******* psdev(): Population standard deviation of data *******
st.pstdev([1.5,2.5,2.5,2.75,3.25,4.75])

# ******* pvariance(): Population variance of data *******
st.pvariance([0.0,0.25,0.25,1.25,1.25])

# ******* stdev(): Sample standard deviration of data *******
st.stdev([1.5,2.5,2.5,2.75,3.25,4.75])

# ******* variance(): Sample variance of data *******
st.variance([0.0,0.25,0.25,1.25,1.5])

###Random Lib###
import random
print(random.random())

print(random.randrange(6))
print(random.choice(['apple','banana']))
print(random.sample(range(100), 5))
print(random.choice('abcdefghij'))

items = [1,2,3,4,5,6,7]
random.shuffle(items)
print(items)

print(random.randint(1,10))
print(random.randrange(0,101,2))
print(random.uniform(1, 100))

###Math Lib###
import math
print('m: %.40f' % math.pi)
print('e: %.40f' % math.e)

print(('arcsine(%.1f) = %5.2f' % (n,math.asin(n)))
print(('arccosine(%.1f) = %5.2f' % (n,math.acos(n)))
print(('arctangent(%.1f) = %5.2f' % (n,math.atan(n)))

n = 100.7
print(math.floor(n))
print(math.ceil(n))

priny(math.fsum(12,6,8))
print(sum([2,6,8]))
print(math.pow(2,3))
print(math.sqrt(9))


