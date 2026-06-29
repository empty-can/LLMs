

# ModelPackageArnDataSource
<a name="API_ModelPackageArnDataSource"></a>

Contains the Amazon Resource Name (ARN) of a SageMaker AI model package to use as the data source for a custom model.

## Contents
<a name="API_ModelPackageArnDataSource_Contents"></a>

 ** modelPackageArn **   <a name="bedrock-Type-ModelPackageArnDataSource-modelPackageArn"></a>
The Amazon Resource Name (ARN) of the SageMaker AI model package. The ARN must be for a model package of `restricted` type.  
To use a model package ARN, you must have the `sagemaker:DescribeModelPackage` and `sagemaker:AccessModelPackageData` permissions on the model package resource.  
Type: String  
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`   
Required: Yes

## See Also
<a name="API_ModelPackageArnDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelPackageArnDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelPackageArnDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelPackageArnDataSource) 