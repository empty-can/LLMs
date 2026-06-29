

# UserIntentCluster
<a name="API_UserIntentCluster"></a>

A cluster of similar user intents identified across sessions.

## Contents
<a name="API_UserIntentCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-UserIntentCluster-affectedSessionCount"></a>
The number of sessions with this user intent.  
Type: Integer  
Required: Yes

 ** affectedSessions **   <a name="BedrockAgentCore-Type-UserIntentCluster-affectedSessions"></a>
The list of sessions with this user intent.  
Type: Array of [UserIntentAffectedSession](API_UserIntentAffectedSession.md) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-UserIntentCluster-clusterId"></a>
The unique identifier of the user intent cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-UserIntentCluster-description"></a>
A description of the user intent pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-UserIntentCluster-name"></a>
The name of the user intent cluster.  
Type: String  
Required: Yes

## See Also
<a name="API_UserIntentCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UserIntentCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UserIntentCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UserIntentCluster) 