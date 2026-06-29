

# CreateGatewayRule
<a name="API_CreateGatewayRule"></a>

Creates a rule for a gateway. Rules define conditions and actions that control how requests are routed and processed through the gateway, including principal-based access control and path-based routing.

## Request Syntax
<a name="API_CreateGatewayRule_RequestSyntax"></a>

```
POST /gateways/{{gatewayIdentifier}}/rules HTTP/1.1
Content-type: application/json

{
   "actions": [ 
      { ... }
   ],
   "clientToken": "{{string}}",
   "conditions": [ 
      { ... }
   ],
   "description": "{{string}}",
   "priority": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateGatewayRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_CreateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-request-uri-gatewayIdentifier"></a>
The identifier of the gateway to create a rule for.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_CreateGatewayRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_CreateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-request-actions"></a>
The actions to take when the rule conditions are met. Actions can route to a specific target or apply a configuration bundle override.  
Type: Array of [Action](API_Action.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** [clientToken](#API_CreateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [conditions](#API_CreateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-request-conditions"></a>
The conditions that must be met for the rule to apply. Conditions can match on principals (IAM ARNs) or request paths.  
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Required: No

 ** [description](#API_CreateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-request-description"></a>
The description of the gateway rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** [priority](#API_CreateGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-request-priority"></a>
The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first. Must be between 1 and 1,000,000.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000000.  
Required: Yes

## Response Syntax
<a name="API_CreateGatewayRule_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_CreateGatewayRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [actions](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-actions"></a>
The actions to take when the rule conditions are met.  
Type: Array of [Action](API_Action.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [conditions](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-conditions"></a>
The conditions that must be met for the rule to apply.  
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.

 ** [createdAt](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-createdAt"></a>
The timestamp when the rule was created.  
Type: Timestamp

 ** [description](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-description"></a>
The description of the gateway rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [gatewayArn](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway that the rule belongs to.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [priority](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-priority"></a>
The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000000.

 ** [ruleId](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-ruleId"></a>
The unique identifier of the gateway rule.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

 ** [status](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-status"></a>
The current status of the rule.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING` 

 ** [system](#API_CreateGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayRule-response-system"></a>
System-managed metadata for rules created by automated processes.  
Type: [SystemManagedBlock](API_SystemManagedBlock.md) object

## Errors
<a name="API_CreateGatewayRule_Errors"></a>

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

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateGatewayRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateGatewayRule) 