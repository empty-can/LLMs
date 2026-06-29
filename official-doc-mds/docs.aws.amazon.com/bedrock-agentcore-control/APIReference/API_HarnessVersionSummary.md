

# HarnessVersionSummary
<a name="API_HarnessVersionSummary"></a>

Summary information about a single version of a harness.

## Contents
<a name="API_HarnessVersionSummary_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-arn"></a>
The ARN of the harness.  
Type: String  
Pattern: `arn:([^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:harness/[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-createdAt"></a>
The timestamp when this harness version was created.  
Type: Timestamp  
Required: Yes

 ** harnessId **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-harnessId"></a>
The ID of the harness.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** harnessName **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-harnessName"></a>
The name of the harness.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}`   
Required: Yes

 ** harnessVersion **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-harnessVersion"></a>
The version of the harness that this summary describes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-status"></a>
The status of this harness version.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-updatedAt"></a>
The timestamp when this harness version was last updated.  
Type: Timestamp  
Required: Yes

 ** failureReason **   <a name="bedrockagentcorecontrol-Type-HarnessVersionSummary-failureReason"></a>
Reason why the create or update operation for this harness version failed.  
Type: String  
Required: No

## See Also
<a name="API_HarnessVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessVersionSummary) 