

# InferenceProfileModelSource
<a name="API_InferenceProfileModelSource"></a>

Contains information about the model or system-defined inference profile that is the source for an inference profile..

## Contents
<a name="API_InferenceProfileModelSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** copyFrom **   <a name="bedrock-Type-InferenceProfileModelSource-copyFrom"></a>
The ARN of the model or system-defined inference profile that is the source for the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|foundation-model)/[a-zA-Z0-9-:.]+`   
Required: No

## See Also
<a name="API_InferenceProfileModelSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/InferenceProfileModelSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/InferenceProfileModelSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/InferenceProfileModelSource) 