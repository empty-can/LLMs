

# GuardrailCrossRegionDetails
<a name="API_GuardrailCrossRegionDetails"></a>

Contains details about the system-defined guardrail profile that you're using with your guardrail for cross-Region inference.

For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).

## Contents
<a name="API_GuardrailCrossRegionDetails_Contents"></a>

 ** guardrailProfileArn **   <a name="bedrock-Type-GuardrailCrossRegionDetails-guardrailProfileArn"></a>
The Amazon Resource Name (ARN) of the guardrail profile that you're using with your guardrail.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail-profile/[a-z0-9-]+[.]{1}guardrail[.]{1}v[0-9:]+`   
Required: No

 ** guardrailProfileId **   <a name="bedrock-Type-GuardrailCrossRegionDetails-guardrailProfileId"></a>
The ID of the guardrail profile that your guardrail is using. Profile availability depends on your current AWS Region. For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html).  
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 30.  
Pattern: `[a-z0-9-]+[.]{1}guardrail[.]{1}v[0-9:]+`   
Required: No

## See Also
<a name="API_GuardrailCrossRegionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailCrossRegionDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailCrossRegionDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailCrossRegionDetails) 