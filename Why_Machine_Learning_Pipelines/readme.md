### Why ML pipelines ??
ML pipelines chains together,  multiple steps so that output of one can be used as an input to other.

It makes easy to apply same processing to train data and the data we are using for the purpose of prediction.

This directory explores both building a model with and without pipelines, and how pipelines makes our life easy.

Video Reference => https://www.youtube.com/watch?v=xOccYkgRV4Q&list=PLKnIA16_RmvYXWH_E6PuVLLHHTWXwwDN7&index=7

#### Why 3 models dumps from Titanic without Pipelines?
Because  => Our Test data require pre-processing of the categorical data that we will send in test data
for ex=> [2, 'male', 31.0, 0, 0, 10.5, 'S'] Now male and S would require encoding and for that we need to have our pre saved dumps for to the 
purpose of processing.

This approach creates  a problem in production code, where based upon input the processing models dumps will change, pipelining resolves this issue as we dont have to create multiple dumps on multiple code changes,
one single dump per change would be enough as everything would be connected to each other in pipes.
