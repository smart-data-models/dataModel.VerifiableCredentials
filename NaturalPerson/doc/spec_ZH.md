<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：自然人  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**自然人的 EBSI 可验证 ID 的模式**  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `credentialSchema[object]`: 包含有关可验证授权所依据的凭证模式（模板）的信息  	- `id[uri]`: 引用存储在（相关）可信模式注册表（TSR）上的凭证模式（模板），可验证授权正是基于该模式进行的    
- `credentialStatus[object]`: 包含有关如何验证可核实证明状态的信息（通过撤销和认可注册表，RER）。  	- `id[uri]`: 撤销和认可注册表 (RER) 中的参考记录，以便核查可核实证明的有效性    
	- `statusListCredential[uri]`: 引用 StatusList2021Credential 的 URL    
	- `statusListIndex[string]`: 以字符串形式表示的整数。基于零的索引值标识状态的位位置    
	- `statusPurpose[string]`: 状态条目的目的    
- `credentialSubject[object]`: 定义可验证 ID 所描述的主体的附加信息  	- `currentAddress[string]`: 定义证书主体的当前地址    
	- `dateOfBirth[date]`: 定义证书主体的出生日期    
	- `familyName[string]`: 定义证书主体的当前姓氏    
	- `firstName[string]`: 定义证书主体当前的名字    
	- `gender[string]`: 定义证书主体的性别    
	- `id[uri]`: 定义可验证证明所述主体的 DID    
	- `nameAndFamilyNameAtBirth[string]`: 定义证书主体出生时的姓氏和名字    
	- `personalIdentifier[string]`: 定义凭证主体的唯一国家标识符（由发送成员国根据用于跨境身份识别的技术规范构建，并尽可能在时间上具有持久性）    
- `evidence[array]`: 包含有关签发可核查证明的程序的信息  - `expirationDate[date-time]`: 定义可验证证明过期的日期和时间  - `id[uri]`: 定义可验证证明的唯一标识符  - `issuanceDate[date-time]`: 定义可验证证明生效的日期和时间  - `issued[date-time]`: 定义可验证证明的签发时间  - `issuer[uri]`: 定义可验证证明的签发人  - `proof[object]`: 包含有关证明的信息  	- `created[date-time]`: 定义创建校样的日期和时间    
	- `jws[string]`: 以 JWS 格式定义证明值    
	- `proofPurpose[string]`: 确定证明的目的    
	- `type[string]`: 定义证明类型    
- `type[array]`: 定义可验证凭据类型  - `validFrom[date-time]`: 定义可验证证明生效的日期和时间  - `validUntil[date-time]`: 定义可验证证明过期的日期和时间  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
源自 EBSI json 模式的数据模型 https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas。@context 属性已从定义中删除，因为它在 NGSI-LD 中是强制性的，不需要明确记录。仅提供键值链接数据中的示例  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NaturalPerson:    
  description: Schema of an EBSI Verifiable ID for a natural person    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialStatus:    
      description: 'Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)'    
      properties:    
        id:    
          description: References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListCredential:    
          description: URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListIndex:    
          description: Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
          x-ngsi:    
            type: Property    
        statusPurpose:    
          description: Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the Verifiable Credential status type    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialSubject:    
      description: Defines additional information about the subject that is described by the Verifiable ID    
      properties:    
        currentAddress:    
          description: Defines the current address of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        dateOfBirth:    
          description: Defines date of birth of the credential subject    
          format: date    
          type: string    
          x-ngsi:    
            type: Property    
        familyName:    
          description: Defines current family name(s) of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        firstName:    
          description: Defines current first name(s) of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        gender:    
          description: Defines the gender of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        nameAndFamilyNameAtBirth:    
          description: Defines the first and the family name(s) of the credential subject at the time of their birth    
          type: string    
          x-ngsi:    
            type: Property    
        personalIdentifier:    
          description: Defines the unique national identifier of the credential subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
          type: string    
          x-ngsi:    
            type: Property    
        placeOfBirth:    
          description: Defines the place where the credential subjectis born    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - familyName    
        - firstName    
        - dateOfBirth    
        - personalIdentifier    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          documentPresence:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          evidenceDocument:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          id:    
            description: 'If present, it MUST contain a URL that points to where more information about this instance of evidence can be found'    
            type: string    
            x-ngsi:    
              type: Property    
          subjectPresence:    
            description: Description to be completed    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Defines the evidence type    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expirationDate:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Defines unique identifier of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    issuanceDate:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issued:    
      description: Defines when the Verifiable Attestation was issued    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issuer:    
      description: Defines the issuer of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        created:    
          description: 'Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        jws:    
          description: Defines the proof value in JWS format    
          type: string    
          x-ngsi:    
            type: Property    
        proofPurpose:    
          description: Defines the purpose of the proof    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the proof type    
          type: string    
          x-ngsi:    
            type: Property    
        verificationMethod:    
          description: Contains information about the verification method / proof mechanisms    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - type    
        - proofPurpose    
        - created    
        - verificationMethod    
        - jws    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: Defines the Verifiable Credential type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validUntil:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - credentialSubject    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-vid/natural-person/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
以 JSON-LD 格式作为键值的 NaturalPerson 示例不可用。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
以 JSON-LD 格式规范化的 NaturalPerson 示例不可用。在不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
#### 自然人 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 NaturalPerson 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:did:123456",  
  "type": ["VerifiableCredential", "VerifiableAttestation", "VerifiableId"],  
  "issuer": "urn:did:9999999",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "issued": "2021-11-01T00:00:00Z",  
  "credentialSubject": {  
    "id": "urn:uri:123",  
    "personalIdentifier": "IT/DE/1234",  
    "familyName": "Castafiori",  
    "firstName": "Bianca",  
    "dateOfBirth": "1930-10-01"  
  },  
  "credentialSchema": {  
    "id": "https://permanent.url.of/vid/naturalperson",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
以 JSON-LD 格式规范化的 NaturalPerson 示例不可用。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
