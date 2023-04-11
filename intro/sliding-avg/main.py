#!/usr/bin/python3

def SlidingAverage(timeseries, k):
  result = [];
  currentSum = sum(timeseries[:k]);
  result.append(currentSum / k);
  for i in range(len(timeseries) - k):
    currentSum -= timeseries[i];
    currentSum += timeseries[i + k];
    currentAvg = currentSum / k;
    result.append(currentAvg);
  return result;

if __name__ == "__main__":
  n  = int(input());
  ts = list(map(int, input().split()));
  k  = int(input());

  res = SlidingAverage(ts, k);

  output = "";

  for i in res:
    output += f"{ i } ";

  output = output[:-1];
  print(output);
