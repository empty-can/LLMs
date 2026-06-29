

# TeacherModelConfig
<a name="API_TeacherModelConfig"></a>

Details about a teacher model used for model customization.

## Contents
<a name="API_TeacherModelConfig_Contents"></a>

 ** teacherModelIdentifier **   <a name="bedrock-Type-TeacherModelConfig-teacherModelIdentifier"></a>
The identifier of the teacher model.  
Type: String  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)$)|([0-9]{12}:inference-profile/[a-zA-Z0-9-:.]+$)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})`   
Required: Yes

 ** maxResponseLengthForInference **   <a name="bedrock-Type-TeacherModelConfig-maxResponseLengthForInference"></a>
The maximum number of tokens requested when the customization job invokes the teacher model.  
Type: Integer  
Required: No

## See Also
<a name="API_TeacherModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TeacherModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TeacherModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TeacherModelConfig) 