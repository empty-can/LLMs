

# UpdateGatewayRule
<a name="API_UpdateGatewayRule"></a>

Updates a gateway rule's priority, conditions, actions, or description.

## Request Syntax
<a name="API_UpdateGatewayRule_RequestSyntax"></a>

```
PATCH /gateways/{{gatewayIdentifier}}/rules/{{ruleId}} HTTP/1.1
Content-type: application/json

{
   "actions": [ 
      { ... }
   ],
   "conditions": [ 
      { ... }
   ],
   "description": "{{string}}",
   "priority": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateGatewayRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_UpdateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-request-uri-gatewayIdentifier"></a>
The identifier of the gateway containing the rule.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [ruleId](#API_UpdateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-request-uri-ruleId"></a>
The unique identifier of the rule to update.  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Request Body
<a name="API_UpdateGatewayRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_UpdateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-request-actions"></a>
The updated actions for the rule.  
Type: Array of [Action](API_Action.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: No

 ** [conditions](#API_UpdateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-request-conditions"></a>
The updated conditions for the rule.  
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Required: No

 ** [description](#API_UpdateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-request-description"></a>
The updated description of the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** [priority](#API_UpdateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-request-priority"></a>
The updated priority of the rule.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000000.  
Required: No

## Response Syntax
<a name="API_UpdateGatewayRule_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "actions": [ 
      { ... }
   ],
   "conditions": [ 
      { ... }
   ],
   "createdAt": "string",
   "description": "string",
   "gatewayArn": "string",
   "priority": number,
   "ruleId": "string",
   "status": "string",
   "system": { 
      "managedBy": "string"
   },
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateGatewayRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [actions](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-actions"></a>
The actions to take when the rule conditions are met.  
Type: Array of [Action](API_Action.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [conditions](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-conditions"></a>
The conditions that must be met for the rule to apply.  
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.

 ** [createdAt](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-createdAt"></a>
The timestamp when the rule was created.  
Type: Timestamp

 ** [description](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-description"></a>
The description of the gateway rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [gatewayArn](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway that the rule belongs to.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [priority](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-priority"></a>
The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000000.

 ** [ruleId](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-ruleId"></a>
The unique identifier of the gateway rule.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

 ** [status](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-status"></a>
The current status of the rule.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING` 

 ** [system](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-system"></a>
System-managed metadata for rules created by automated processes.  
Type: [SystemManagedBlock](API_SystemManagedBlock.md) object

 ** [updatedAt](#API_UpdateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayRule-response-updatedAt"></a>
The timestamp when the rule was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdateGatewayRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateGatewayRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule) 