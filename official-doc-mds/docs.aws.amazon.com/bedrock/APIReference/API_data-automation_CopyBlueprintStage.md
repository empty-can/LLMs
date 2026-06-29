

# CopyBlueprintStage
<a name="API_data-automation_CopyBlueprintStage"></a>

Copies a blueprint from one stage to another.

## Request Syntax
<a name="API_data-automation_CopyBlueprintStage_RequestSyntax"></a>

```
PUT /blueprints/{{blueprintArn}}/copy-stage HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "sourceStage": "{{string}}",
   "targetStage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_CopyBlueprintStage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [blueprintArn](#API_data-automation_CopyBlueprintStage_RequestSyntax) **   <a name="bedrock-data-automation_CopyBlueprintStage-request-uri-blueprintArn"></a>
The blueprint's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: Yes

## Request Body
<a name="API_data-automation_CopyBlueprintStage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_data-automation_CopyBlueprintStage_RequestSyntax) **   <a name="bedrock-data-automation_CopyBlueprintStage-request-clientToken"></a>
To avoid creating duplicate resources, specify a unique token for this operation.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [sourceStage](#API_data-automation_CopyBlueprintStage_RequestSyntax) **   <a name="bedrock-data-automation_CopyBlueprintStage-request-sourceStage"></a>
The stage to copy from.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: Yes

 ** [targetStage](#API_data-automation_CopyBlueprintStage_RequestSyntax) **   <a name="bedrock-data-automation_CopyBlueprintStage-request-targetStage"></a>
The stage to copy to.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: Yes

## Response Syntax
<a name="API_data-automation_CopyBlueprintStage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_data-automation_CopyBlueprintStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_data-automation_CopyBlueprintStage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_CopyBlueprintStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/CopyBlueprintStage) 