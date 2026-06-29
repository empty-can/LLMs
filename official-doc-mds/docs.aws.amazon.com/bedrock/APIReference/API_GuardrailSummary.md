

# GuardrailSummary
<a name="API_GuardrailSummary"></a>

Contains details about a guardrail.

This data type is used in the following API operations:
+  [ListGuardrails response body](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListGuardrails.html#API_ListGuardrails_ResponseSyntax) 

## Contents
<a name="API_GuardrailSummary_Contents"></a>

 ** arn **   <a name="bedrock-Type-GuardrailSummary-arn"></a>
The ARN of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-GuardrailSummary-createdAt"></a>
The date and time at which the guardrail was created.  
Type: Timestamp  
Required: Yes

 ** id **   <a name="bedrock-Type-GuardrailSummary-id"></a>
The unique identifier of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: Yes

 ** name **   <a name="bedrock-Type-GuardrailSummary-name"></a>
The name of the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[0-9a-zA-Z-_]+`   
Required: Yes

 ** status **   <a name="bedrock-Type-GuardrailSummary-status"></a>
The status of the guardrail.  
Type: String  
Valid Values: `CREATING | UPDATING | VERSIONING | READY | FAILED | DELETING`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-GuardrailSummary-updatedAt"></a>
The date and time at which the guardrail was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="bedrock-Type-GuardrailSummary-version"></a>
The version of the guardrail.  
Type: String  
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))`   
Required: Yes

 ** crossRegionDetails **   <a name="bedrock-Type-GuardrailSummary-crossRegionDetails"></a>
Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).  
Type: [GuardrailCrossRegionDetails](API_GuardrailCrossRegionDetails.md) object  
Required: No

 ** description **   <a name="bedrock-Type-GuardrailSummary-description"></a>
A description of the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_GuardrailSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailSummary) 