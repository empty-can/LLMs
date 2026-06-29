

# HarnessEndpoint
<a name="API_HarnessEndpoint"></a>

Representation of a harness endpoint. An endpoint is a named, stable reference to a specific version of a harness that callers invoke, allowing the underlying version to be updated without changing how the agent is invoked.

## Contents
<a name="API_HarnessEndpoint_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-arn"></a>
The ARN of the endpoint.  
Type: String  
Pattern: `arn:([^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:harness/[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}/endpoint/[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-createdAt"></a>
The timestamp when the endpoint was created.  
Type: Timestamp  
Required: Yes

 ** endpointName **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-endpointName"></a>
The name of the endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** harnessId **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-harnessId"></a>
The ID of the harness that the endpoint belongs to.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** harnessName **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-harnessName"></a>
The name of the harness that the endpoint belongs to.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-status"></a>
The status of the endpoint.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-updatedAt"></a>
The timestamp when the endpoint was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-description"></a>
The description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** failureReason **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-failureReason"></a>
The reason the endpoint's last create or update operation failed.  
Type: String  
Required: No

 ** liveVersion **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-liveVersion"></a>
The harness version that the endpoint is currently serving.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

 ** targetVersion **   <a name="bedrockagentcorecontrol-Type-HarnessEndpoint-targetVersion"></a>
The harness version that the endpoint points to. While an update is in progress, this can differ from the live version until the endpoint finishes transitioning.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

## See Also
<a name="API_HarnessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessEndpoint) 