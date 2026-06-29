

# SageMakerEndpoint
<a name="API_SageMakerEndpoint"></a>

Specifies the configuration for a Amazon SageMaker endpoint.

## Contents
<a name="API_SageMakerEndpoint_Contents"></a>

 ** executionRole **   <a name="bedrock-Type-SageMakerEndpoint-executionRole"></a>
The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on Amazon EC2 compute instances or for batch transform jobs.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** initialInstanceCount **   <a name="bedrock-Type-SageMakerEndpoint-initialInstanceCount"></a>
The number of Amazon EC2 compute instances to deploy for initial endpoint creation.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: Yes

 ** instanceType **   <a name="bedrock-Type-SageMakerEndpoint-instanceType"></a>
The Amazon EC2 compute instance type to deploy for hosting the model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** kmsEncryptionKey **   <a name="bedrock-Type-SageMakerEndpoint-kmsEncryptionKey"></a>
The AWS KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the Amazon EC2 compute instance that hosts the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** vpc **   <a name="bedrock-Type-SageMakerEndpoint-vpc"></a>
The VPC configuration for the endpoint.  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## See Also
<a name="API_SageMakerEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/SageMakerEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/SageMakerEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/SageMakerEndpoint) 