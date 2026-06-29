

# Finding
<a name="API_Finding"></a>

Represents a finding or issue discovered during policy generation or validation. Findings provide insights about potential problems, recommendations, or validation results from policy analysis operations. Finding types include: VALID (policy is ready to use), INVALID (policy has validation errors that must be fixed), NOT\_TRANSLATABLE (input couldn't be converted to policy), ALLOW\_ALL (policy would allow all actions, potential security risk), ALLOW\_NONE (policy would allow no actions, unusable), DENY\_ALL (policy would deny all actions, may be too restrictive), and DENY\_NONE (policy would deny no actions, ineffective). Review all findings before creating policies from generated assets to ensure they match your security requirements.

## Contents
<a name="API_Finding_Contents"></a>

 ** description **   <a name="bedrockagentcorecontrol-Type-Finding-description"></a>
A human-readable description of the finding. This provides detailed information about the issue, recommendation, or validation result to help users understand and address the finding.   
Type: String  
Required: No

 ** type **   <a name="bedrockagentcorecontrol-Type-Finding-type"></a>
The type or category of the finding. This classifies the finding as an error, warning, recommendation, or informational message to help users understand the severity and nature of the issue.  
Type: String  
Valid Values: `VALID | INVALID | NOT_TRANSLATABLE | ALLOW_ALL | ALLOW_NONE | DENY_ALL | DENY_NONE`   
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Finding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Finding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Finding) 