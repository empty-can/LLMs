

# CustomModelDataSource
<a name="API_CustomModelDataSource"></a>

The data source for a custom model. This is a union type that supports the following member:
+  `modelPackageArnDataSource` — Specifies a SageMaker AI model package as the data source.

## Contents
<a name="API_CustomModelDataSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** modelPackageArnDataSource **   <a name="bedrock-Type-CustomModelDataSource-modelPackageArnDataSource"></a>
A SageMaker AI model package ARN as the data source for the custom model. When you specify a model package ARN, Amazon Bedrock resolves the model package to retrieve the model artifacts.  
Type: [ModelPackageArnDataSource](API_ModelPackageArnDataSource.md) object  
Required: No

## See Also
<a name="API_CustomModelDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomModelDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomModelDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomModelDataSource) 