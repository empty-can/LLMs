

# ABTestSummary
<a name="API_ABTestSummary"></a>

Summary information about an A/B test.

## Contents
<a name="API_ABTestSummary_Contents"></a>

 ** abTestArn **   <a name="BedrockAgentCore-Type-ABTestSummary-abTestArn"></a>
The Amazon Resource Name (ARN) of the A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** abTestId **   <a name="BedrockAgentCore-Type-ABTestSummary-abTestId"></a>
The unique identifier of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-ABTestSummary-createdAt"></a>
The timestamp when the A/B test was created.  
Type: Timestamp  
Required: Yes

 ** executionStatus **   <a name="BedrockAgentCore-Type-ABTestSummary-executionStatus"></a>
The execution status of the A/B test.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED`   
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-ABTestSummary-name"></a>
The name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-ABTestSummary-status"></a>
The current status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-ABTestSummary-updatedAt"></a>
The timestamp when the A/B test was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-ABTestSummary-description"></a>
The description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** gatewayArn **   <a name="BedrockAgentCore-Type-ABTestSummary-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway used for traffic splitting.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: No

## See Also
<a name="API_ABTestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ABTestSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ABTestSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ABTestSummary) 