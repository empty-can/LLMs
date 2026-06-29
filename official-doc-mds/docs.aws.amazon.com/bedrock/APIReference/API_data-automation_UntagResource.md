

# UntagResource
<a name="API_data-automation_UntagResource"></a>

Remove the tags from a resource.

## Request Syntax
<a name="API_data-automation_UntagResource_RequestSyntax"></a>

```
POST /untagResource HTTP/1.1
Content-type: application/json

{
   "resourceARN": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_data-automation_UntagResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_UntagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceARN](#API_data-automation_UntagResource_RequestSyntax) **   <a name="bedrock-data-automation_UntagResource-request-resourceARN"></a>
The ARN of the resource you want to untag.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-z0-9-]*:[0-9]{12}:(blueprint|data-automation-project|blueprint-optimization-invocation|data-automation-library|data-automation-library-ingestion-job)/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** [tagKeys](#API_data-automation_UntagResource_RequestSyntax) **   <a name="bedrock-data-automation_UntagResource-request-tagKeys"></a>
The keys of the tag you want to untag.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Syntax
<a name="API_data-automation_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_data-automation_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_data-automation_UntagResource_Errors"></a>

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
<a name="API_data-automation_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/UntagResource) 