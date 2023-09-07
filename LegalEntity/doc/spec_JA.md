<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティエンティティ  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/LegalEntity/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**法人の EBSI 検証可能 ID のスキーマ**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `credentialSchema[object]`: 検証可能な認証が基づくクレデンシャル・スキーマ（テンプレート）に関する情報が含まれる。  	- `id[uri]`: 検証可能な認可が基づく（関連する）信頼スキーマ・レジストリ（TSR）に格納されているクレ デンシャル・スキーマ（テンプレート）を参照する。    
- `credentialStatus[object]`: 検証可能な証明のステータスを確認する方法に関する情報を含む（失効および裏書レジストリ（RER）を通じて）。  	- `id[uri]`: 検証可能な認証の有効性を検証できるようにするため、失効および裏書レジストリ（RER）の 記録を参照する。    
	- `statusListCredential[uri]`: StatusList2021Credential を参照する URL。    
	- `statusListIndex[string]`: 文字列として表現される整数。ゼロベースのインデックス値は、ステータスのビット位置を示す。    
	- `statusPurpose[string]`: ステータスエントリーの目的    
- `credentialSubject[object]`: 検証可能 ID が記述する対象者に関する情報を定義する。  	- `EORI[string]`: クレデンシャル対象者の経済的事業者登録および識別（EORI）（欧州委員会施行規則（EU）No 1352/2013 に言及）    
	- `LEI[string]`: クレデンシャル対象者の正式な法人識別子（LEI）（欧州委員会施行規則（EU）No 1247/2012 で言及）。    
	- `SEED[string]`: クレデンシャル対象者の物品データ交換システム（SEED）（すなわち、理事会規則 （EC）No 389/2012 の第 2 条(12)に規定される物品番号）。    
	- `SIC[string]`: 資格対象者の標準産業分類（SIC）（欧州議会および理事会指令 2009/101/EC の第 3 条(1)）。    
	- `VATRegistration[string]`: 資格対象者のVAT番号    
	- `domainName[string]`: クレデンシャル・サブジェクトのドメイン名    
	- `id[uri]`: 検証可能な証明によって記述される対象の DID を定義する。    
	- `identifier[array]`: 記入すべき内容    
	- `legalAddress[string]`: クレデンシャル対象者の正式な法的住所    
	- `legalName[string]`: クレデンシャル対象者の正式な法的名称    
	- `legalPersonIdentifier[string]`: クレデンシャル対象者の国内/法定識別子（送信側加盟国が国境を越えた識別を目的として技術 仕様に従って構築したもので、時間的に可能な限り永続的なもの）。    
- `evidence[array]`: 検証可能な証明書の発行に至ったプロセスに関する情報を含む。  - `expirationDate[date-time]`: 検証可能証明の有効期限が切れる日時を定義する。  - `id[uri]`: 検証可能証明の一意な識別子を定義する。  - `issuanceDate[date-time]`: 検証可能な認証が有効になる日時を定義する。  - `issued[date-time]`: 検証可能な証明書がいつ発行されたかを定義する。  - `issuer[uri]`: 検証可能な証明の発行者を定義する。  - `proof[object]`: 証明に関する情報を含む  	- `created[date-time]`: プルーフが作成された日時を定義します。    
	- `jws[string]`: JWSフォーマットで証明値を定義します。    
	- `proofPurpose[string]`: 証明の目的を明確にする    
	- `type[string]`: 証明タイプを定義する    
- `type[array]`: 検証可能クレデンシャルタイプを定義する。  - `validFrom[date-time]`: 検証可能な認証が有効になる日時を定義する。  - `validUntil[date-time]`: 検証可能証明の有効期限が切れる日時を定義する。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
EBSI jsonスキーマから派生したデータモデル https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas.context属性はNGSI-LDでは必須であり、明示的に文書化する必要がないため、定義から削除された。キー値リンクデータの例のみ利用可能  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
LegalEntity:    
  description: Schema of an EBSI Verifiable ID for a legal entity    
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
      description: Defines information about the subject that is described by the Verifiable ID    
      properties:    
        EORI:    
          description: Economic Operator Registration and Identification (EORI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1352/2013)    
          type: string    
          x-ngsi:    
            type: Property    
        LEI:    
          description: Official legal entity identifier (LEI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1247/2012)    
          type: string    
          x-ngsi:    
            type: Property    
        SEED:    
          description: System for Exchange of Excise Data (SEED) of Credential Subject (i.e. excise number provided in Article 2(12) of Council Regulation (EC) No 389/2012)    
          type: string    
          x-ngsi:    
            type: Property    
        SIC:    
          description: Standard Industrial Classification (SIC) of Credential Subject (Article 3(1) of Directive 2009/101/EC of the European Parliament and of the Council.)    
          type: string    
          x-ngsi:    
            type: Property    
        VATRegistration:    
          description: VAT number  of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        domainName:    
          description: Domain name  of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        identifier:    
          description: Description to be completed    
          items:    
            properties:    
              id:    
                description: Description to be completed    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
              schemeID:    
                description: Description to be completed    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: Description to be completed    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
        legalAddress:    
          description: Official legal address of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        legalName:    
          description: Official legal name of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        legalPersonIdentifier:    
          description: National/Legal Identifier of Credential Subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
          type: string    
          x-ngsi:    
            type: Property    
        taxReference:    
          description: Official tax reference number of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - legalName    
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
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-vid/legal-entity/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/LegalEntity/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のLegalEntityの例をkey-valuesとして利用することはできない。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の LegalEntity の例は利用できない。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返す。  
#### LegalEntity NGSI-LD キー値の例  
JSON-LD形式のLegalEntityのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "https://www.w3.org/2018/credentials/v1",  
    "https://europa.eu/schemas/v-id/2020/v1",  
    "https://europa.eu/schemas/eidas/2020/v1"  
  ],  
  "id": "urn:did:123456",  
  "type": ["VerifiableCredential", "VerifiableAttestation"],  
  "issuer": "did:ebsi:2757945549477fc571663bee12042873fe555b674bd294a3",  
  "issuanceDate": "2019-06-22T14:11:44Z",  
  "validFrom": "2019-06-22T14:11:44Z",  
  "issued": "2019-06-22T14:11:44Z",  
  "credentialSubject": {  
    "id": "did:ebsi:2659b154a445434a39d91149ead3bd993cb99fd5e78281b7",  
    "identifier": [  
      {  
        "schemeID": "SHACL",  
        "value": "SHACL ID 1",  
        "id": "http://student.id/41231232"  
      }  
    ],  
    "legalName": "Example Company"  
  },  
  "credentialStatus": {  
    "id": "https://europa.eu/status/identity#1dee355d-0432-4910-ac9c-70d89e8d674e",  
    "type": "CredentialStatusList2020"  
  },  
  "credentialSchema": {  
    "id": "https://europa.eu/tsr-vid/verifiableid1.json",  
    "type": "FullJsonSchemaValidator2021"  
  },  
  "evidence": [  
    {  
      "id": "https://europa.eu/tsr-vid/evidence/f2aeec97-fc0d-42bf-8ca7-0548192d4231",  
      "type": ["DocumentVerification"],  
      "verifier": "did:ebsi:2e81454f76775c687694ee6772a17796436768a30e289555",  
      "evidenceDocument": ["Passport"],  
      "subjectPresence": "Physical",  
      "documentPresence": ["Physical"]  
    }  
  ],  
  "proof": {  
    "type": "EidasSeal2021",  
    "created": "2019-06-22T14:11:44Z",  
    "proofPurpose": "assertionMethod",  
    "verificationMethod": "did:ebsi:2757945549477fc571663bee12042873fe555b674bd294a3#2368332668",  
    "jws": "HG21J4fdlnBvBA+y6D...amP7O="  
  }  
}  
```  
</details>  
正規化された JSON-LD 形式の LegalEntity の例は利用できない。これは、オプションを使用しない場合は NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
