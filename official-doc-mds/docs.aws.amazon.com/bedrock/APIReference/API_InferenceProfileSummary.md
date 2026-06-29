

# InferenceProfileSummary
<a name="API_InferenceProfileSummary"></a>

Contains information about an inference profile.

## Contents
<a name="API_InferenceProfileSummary_Contents"></a>

 ** inferenceProfileArn **   <a name="bedrock-Type-InferenceProfileSummary-inferenceProfileArn"></a>
The Amazon Resource Name (ARN) of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+`   
Required: Yes

 ** inferenceProfileId **   <a name="bedrock-Type-InferenceProfileSummary-inferenceProfileId"></a>
The unique identifier of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-:.]+`   
Required: Yes

 ** inferenceProfileName **   <a name="bedrock-Type-InferenceProfileSummary-inferenceProfileName"></a>
The name of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `([0-9a-zA-Z][ _-]?)+`   
Required: Yes

 ** models **   <a name="bedrock-Type-InferenceProfileSummary-models"></a>
A list of information about each model in the inference profile.  
Type: Array of [InferenceProfileModel](API_InferenceProfileModel.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** status **   <a name="bedrock-Type-InferenceProfileSummary-status"></a>
The status of the inference profile. `ACTIVE` means that the inference profile is ready to be used.  
Type: String  
Valid Values: `ACTIVE`   
Required: Yes

 ** type **   <a name="bedrock-Type-InferenceProfileSummary-type"></a>
The type of the inference profile. The following types are possible:  
+  `SYSTEM_DEFINED` – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.
+  `APPLICATION` – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.
Type: String  
Valid Values: `SYSTEM_DEFINED | APPLICATION`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-InferenceProfileSummary-createdAt"></a>
The time at which the inference profile was created.  
Type: Timestamp  
Required: No

 ** description **   <a name="bedrock-Type-InferenceProfileSummary-description"></a>
The description of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `([0-9a-zA-Z:.][ _-]?)+`   
Required: No

 ** updatedAt **   <a name="bedrock-Type-InferenceProfileSummary-updatedAt"></a>
The time at which the inference profile was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_InferenceProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/InferenceProfileSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/InferenceProfileSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/InferenceProfileSummary) 