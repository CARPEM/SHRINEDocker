<map version="freeplane 1.6.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="OSIRIS" FOLDED="false" ID="ID_0" CREATED="1541758553111" MODIFIED="1541758553111"><hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" show_icon_for_attributes="true" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<node TEXT="Patient" POSITION="right" ID="ID_2" CREATED="1541758553111" MODIFIED="1541758553111">
<icon BUILTIN="male1"/>
<node TEXT="Gender" ID="ID_4" CREATED="1541758553111" MODIFIED="1541760322868">
<attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/Patient_Gender#conceptualdomain" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/Patient_Gender#conceptualdomain"/>
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="Ethnicity" FOLDED="true" ID="ID_5" CREATED="1541758553111" MODIFIED="1541758553111">
<attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/Patient_Ethnicity#conceptualdomain" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/Patient_Ethnicity#conceptualdomain"/>
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="BirthDate" FOLDED="true" ID="ID_6" CREATED="1541758553111" MODIFIED="1541758553111">
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="DeathDate" FOLDED="true" ID="ID_7" CREATED="1541758553111" MODIFIED="1541758553111">
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="ProviderCenterId" FOLDED="true" ID="ID_8" CREATED="1541758553111" MODIFIED="1541758553111">
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="OriginCenterId" FOLDED="true" ID="ID_9" CREATED="1541758553111" MODIFIED="1541758553111">
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="CauseOfDeath" FOLDED="true" ID="ID_10" CREATED="1541758553111" MODIFIED="1541758553111">
<attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/Patient_CauseOfDeath#conceptualdomain" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/Patient_CauseOfDeath#conceptualdomain"/>
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="LastNewsDate" FOLDED="true" ID="ID_11" CREATED="1541758553112" MODIFIED="1541758553112">
<attribute NAME="concept" VALUE="Patient" />
</node>
<node TEXT="LastNewsStatus" FOLDED="true" ID="ID_12" CREATED="1541758553112" MODIFIED="1541758553112">
<attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/Patient_LastNewsStatus#conceptualdomain" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/Patient_LastNewsStatus#conceptualdomain"/>
<attribute NAME="concept" VALUE="Patient" />
</node>
</node>
<node TEXT="tumorPathologyEvent" POSITION="right" ID="ID_14" CREATED="1541758553112" MODIFIED="1541758553112">
<icon BUILTIN="bookmark"/>
<node TEXT="Type" FOLDED="true" ID="ID_15" CREATED="1541758553112" MODIFIED="1541758553112">
<attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/TumorPathologyEvent_Type#conceptualdomain" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/TumorPathologyEvent_Type#conceptualdomain"/>
<attribute NAME="concept" VALUE="TumorPathologyEvent" />
</node>
<node TEXT="StartDate" FOLDED="true" ID="ID_16" CREATED="1541758553112" MODIFIED="1541758553112"/>
<node TEXT="EndDate" FOLDED="true" ID="ID_17" CREATED="1541758553112" MODIFIED="1541758553112"/>
<node TEXT="PerformanceStatus" FOLDED="true" ID="ID_18" CREATED="1541758553112" MODIFIED="1541758553112">
<attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/TumorPathologyEvent_PerformanceStatus#conceptualdomain" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/TumorPathologyEvent_PerformanceStatus#conceptualdomain"/>
<attribute NAME="concept" VALUE="TumorPathologyEvent" />
</node>
<node TEXT="G8" FOLDED="true" ID="ID_19" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="HistologicalGradeType" FOLDED="true" ID="ID_20" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="HistologicalGradeValue" FOLDED="true" ID="ID_21" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="StadeType" FOLDED="true" ID="ID_22" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="StadeValue" FOLDED="true" ID="ID_23" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="DiagnosisDate" FOLDED="true" ID="ID_24" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="TopographyCode" FOLDED="true" ID="ID_25" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="MorphologyCode" FOLDED="true" ID="ID_26" CREATED="1541758553113" MODIFIED="1541758553113"/>
<node TEXT="Laterality" FOLDED="true" ID="ID_27" CREATED="1541758553113" MODIFIED="1541758553113"/>
</node>
<node TEXT="TNM" POSITION="right" ID="ID_28" CREATED="1541758553113" MODIFIED="1541758553113">
  <node TEXT="T" FOLDED="true" ID="ID_29" CREATED="1541758553113" MODIFIED="1541758553113">
    <icon BUILTIN="messagebox_warning"/>
    <attribute NAME="modality" VALUE="https://github.com/siric-osiris/OSIRIS/wiki/TNM_T" OBJECT="java.net.URI|https://github.com/siric-osiris/OSIRIS/wiki/TNM_T"/>
    <attribute NAME="concept" VALUE="TNM" />
  </node>
  <node TEXT="N" FOLDED="true" ID="ID_30" CREATED="1541758553114" MODIFIED="1541758553114">
    <icon BUILTIN="messagebox_warning"/>
  </node>
  <node TEXT="M" FOLDED="true" ID="ID_31" CREATED="1541758553114" MODIFIED="1541758553114">
    <icon BUILTIN="messagebox_warning"/>
  </node>
  <node TEXT="TNMVersion" FOLDED="true" ID="ID_32" CREATED="1541758553114" MODIFIED="1541758553114">
    <icon BUILTIN="messagebox_warning"/>
  </node>
  <node TEXT="TNMType" FOLDED="true" ID="ID_33" CREATED="1541758553114" MODIFIED="1541758553114">
    <icon BUILTIN="messagebox_warning"/>
  </node>
</node>
<node TEXT="Treatment" POSITION="right" ID="ID_34" CREATED="1541758553114" MODIFIED="1541758553114">
<node TEXT="Type" FOLDED="true" ID="ID_35" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="LineNumber" FOLDED="true" ID="ID_36" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ActivityCode" FOLDED="true" ID="ID_37" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="StartDate" FOLDED="true" ID="ID_38" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="EndDate" FOLDED="true" ID="ID_39" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ClinicalTrialContext" FOLDED="true" ID="ID_40" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ClinicalTrialName" FOLDED="true" ID="ID_41" CREATED="1541758553114" MODIFIED="1541758553114">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ClinicalTrialId" FOLDED="true" ID="ID_42" CREATED="1541758553115" MODIFIED="1541758553115">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="SurgeryResectionQuality" FOLDED="true" ID="ID_43" CREATED="1541758553115" MODIFIED="1541758553115">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="SurgeryNature" FOLDED="true" ID="ID_44" CREATED="1541758553115" MODIFIED="1541758553115">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ResponseEvaluation" FOLDED="true" ID="ID_45" CREATED="1541758553115" MODIFIED="1541758553115">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Date" FOLDED="true" ID="ID_46" CREATED="1541758553115" MODIFIED="1541758553115">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Status" FOLDED="true" ID="ID_47" CREATED="1541758553115" MODIFIED="1541758553115">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
</node>
<node TEXT="ResponseEvaluation" POSITION="right" ID="ID_48" CREATED="1541758553116" MODIFIED="1541758553116">
<node TEXT="Date" FOLDED="true" ID="ID_49" CREATED="1541758553116" MODIFIED="1541758553116">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Status" FOLDED="true" ID="ID_50" CREATED="1541758553116" MODIFIED="1541758553116">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="AdverseEvent" POSITION="right" ID="ID_51" CREATED="1541758553116" MODIFIED="1541758553116">
<node TEXT="Code" FOLDED="true" ID="ID_52" CREATED="1541758553116" MODIFIED="1541758553116">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Date" FOLDED="true" ID="ID_53" CREATED="1541758553116" MODIFIED="1541758553116">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="EndDate" FOLDED="true" ID="ID_54" CREATED="1541758553116" MODIFIED="1541758553116">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Grade" FOLDED="true" ID="ID_55" CREATED="1541758553116" MODIFIED="1541758553116">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="BiologicalSample" POSITION="right" ID="ID_199" CREATED="1541758553116" MODIFIED="1541758553116">
<node TEXT="SampleExternalAccession" ID="ID_200" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ParentSampleExternalAccession" ID="ID_201" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="CollectDate" ID="ID_202" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="TopographyCode" ID="ID_203" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Nature" ID="ID_204" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Origin" ID="ID_205" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="StorageTemperature" ID="ID_206" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="TumorCellularity" ID="ID_207" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Biomarker" POSITION="right" ID="ID_208" CREATED="1541758553117" MODIFIED="1541758553117">
<node TEXT="Code" ID="ID_209" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Value" ID="ID_210" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Unit" ID="ID_211" CREATED="1541758553117" MODIFIED="1541758553117">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Drug" POSITION="right" ID="ID_56" CREATED="1541758553118" MODIFIED="1541758553118">
<node TEXT="Code" FOLDED="true" ID="ID_57" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Name" FOLDED="true" ID="ID_58" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Treatment" FOLDED="true" ID="ID_59" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_60" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="LineNumber" FOLDED="true" ID="ID_61" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ActivityCode" FOLDED="true" ID="ID_62" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="StartDate" FOLDED="true" ID="ID_63" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="EndDate" FOLDED="true" ID="ID_64" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ClinicalTrialContext" FOLDED="true" ID="ID_65" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ClinicalTrialName" FOLDED="true" ID="ID_66" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ClinicalTrialId" FOLDED="true" ID="ID_67" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="SurgeryResectionQuality" FOLDED="true" ID="ID_68" CREATED="1541758553118" MODIFIED="1541758553118">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="SurgeryNature" FOLDED="true" ID="ID_69" CREATED="1541758553119" MODIFIED="1541758553119">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
</node>
<node TEXT="Consent" FOLDED="true" POSITION="right" ID="ID_70" CREATED="1541758553119" MODIFIED="1541758553119">
<node TEXT="Date" FOLDED="true" ID="ID_71" CREATED="1541758553119" MODIFIED="1541758553119">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GeneticAnalysisAuthorization" FOLDED="true" ID="ID_72" CREATED="1541758553119" MODIFIED="1541758553119">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="RelatedPathology" FOLDED="true" POSITION="right" ID="ID_73" CREATED="1541758553119" MODIFIED="1541758553119">
<node TEXT="PathologyCode" FOLDED="true" ID="ID_74" CREATED="1541758553119" MODIFIED="1541758553119">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="DiagnosisDate" FOLDED="true" ID="ID_75" CREATED="1541758553119" MODIFIED="1541758553119">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="PathologyEndDate" FOLDED="true" ID="ID_76" CREATED="1541758553119" MODIFIED="1541758553119">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="FamilyCancerHistory" FOLDED="true" POSITION="right" ID="ID_77" CREATED="1541758553119" MODIFIED="1541758553119">
<node TEXT="TopographyCode" FOLDED="true" ID="ID_78" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Parentage" FOLDED="true" ID="ID_79" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Annotation" FOLDED="true" POSITION="right" ID="ID_80" CREATED="1541758553120" MODIFIED="1541758553120">
<node TEXT="AlterationType" FOLDED="true" ID="ID_81" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ReferenceType" FOLDED="true" ID="ID_82" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ReferenceDatabase" FOLDED="true" ID="ID_83" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ReferenceValue" FOLDED="true" ID="ID_84" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="PfamDomain" FOLDED="true" ID="ID_85" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="PfamId" FOLDED="true" ID="ID_86" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="MutationPredictionAlgorithm" FOLDED="true" ID="ID_87" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="MutationPredictionValue" FOLDED="true" ID="ID_88" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="MutationPredictionScore" FOLDED="true" ID="ID_89" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="DNARegionName" FOLDED="true" ID="ID_90" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="DNASequenceVariation" FOLDED="true" ID="ID_91" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AminoAcidChange" FOLDED="true" ID="ID_92" CREATED="1541758553120" MODIFIED="1541758553120">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicSequenceVariation" FOLDED="true" ID="ID_93" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="RNASequenceVariation" FOLDED="true" ID="ID_94" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AminoAcidChangeType" FOLDED="true" ID="ID_95" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="FusionPrimeEnd" FOLDED="true" ID="ID_96" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Strand" FOLDED="true" ID="ID_97" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Symbol" FOLDED="true" ID="ID_98" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AlterationOnSample" FOLDED="true" ID="ID_99" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Pathogenicity" FOLDED="true" ID="ID_100" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Actionability" FOLDED="true" ID="ID_101" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ProposedForOrientation" FOLDED="true" ID="ID_102" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Variant" FOLDED="true" ID="ID_103" CREATED="1541758553121" MODIFIED="1541758553121">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Alteration" FOLDED="true" ID="ID_104" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Chromosome" FOLDED="true" ID="ID_105" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStart" FOLDED="true" ID="ID_106" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStop" FOLDED="true" ID="ID_107" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomeBuild" FOLDED="true" ID="ID_108" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Cytoband" FOLDED="true" ID="ID_109" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="ReferenceAllele" FOLDED="true" ID="ID_110" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AlternativeAllele" FOLDED="true" ID="ID_111" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="DNASequenceVariationType" FOLDED="true" ID="ID_112" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="VariantInSample" FOLDED="true" ID="ID_113" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="PositionReadDepth" FOLDED="true" ID="ID_114" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="VariantReadDepth" FOLDED="true" ID="ID_115" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="StrandBias" FOLDED="true" ID="ID_116" CREATED="1541758553122" MODIFIED="1541758553122">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicSourceClass" FOLDED="true" ID="ID_117" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AllelicState" FOLDED="true" ID="ID_118" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
</node>
<node TEXT="Validation" FOLDED="true" ID="ID_119" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_120" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Method" FOLDED="true" ID="ID_121" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Status" FOLDED="true" ID="ID_122" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="CNV" FOLDED="true" ID="ID_123" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Alteration" FOLDED="true" ID="ID_124" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Chromosome" FOLDED="true" ID="ID_125" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStart" FOLDED="true" ID="ID_126" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStop" FOLDED="true" ID="ID_127" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomeBuild" FOLDED="true" ID="ID_128" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Cytoband" FOLDED="true" ID="ID_129" CREATED="1541758553123" MODIFIED="1541758553123">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="SegmentIntensity" FOLDED="true" ID="ID_130" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="SegmentGenomicStatus" FOLDED="true" ID="ID_131" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="CopyNumber" FOLDED="true" ID="ID_132" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="LOH" FOLDED="true" ID="ID_133" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Fusion" FOLDED="true" ID="ID_134" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_135" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Point5prime" FOLDED="true" ID="ID_136" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Point3prime" FOLDED="true" ID="ID_137" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="InFrame" FOLDED="true" ID="ID_138" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="NbSpanningPair" FOLDED="true" ID="ID_139" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="NbSplitReads" FOLDED="true" ID="ID_140" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Expression" FOLDED="true" ID="ID_141" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="GenomeEntity" FOLDED="true" ID="ID_142" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_143" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Database" FOLDED="true" ID="ID_144" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Id" FOLDED="true" ID="ID_145" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Symbol" FOLDED="true" ID="ID_146" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="GeneDataType" FOLDED="true" ID="ID_147" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GeneValue" FOLDED="true" ID="ID_148" CREATED="1541758553124" MODIFIED="1541758553124">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
</node>
</node>
<node TEXT="AlterationOnSample" FOLDED="true" POSITION="right" ID="ID_149" CREATED="1541758553125" MODIFIED="1541758553125">
<node TEXT="Pathogenicity" FOLDED="true" ID="ID_150" CREATED="1541758553125" MODIFIED="1541758553125">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Actionability" FOLDED="true" ID="ID_151" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="ProposedForOrientation" FOLDED="true" ID="ID_152" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Variant" FOLDED="true" ID="ID_153" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Alteration" FOLDED="true" ID="ID_154" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Chromosome" FOLDED="true" ID="ID_155" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStart" FOLDED="true" ID="ID_156" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStop" FOLDED="true" ID="ID_157" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomeBuild" FOLDED="true" ID="ID_158" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Cytoband" FOLDED="true" ID="ID_159" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="ReferenceAllele" FOLDED="true" ID="ID_160" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AlternativeAllele" FOLDED="true" ID="ID_161" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="DNASequenceVariationType" FOLDED="true" ID="ID_162" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="VariantInSample" FOLDED="true" ID="ID_163" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="PositionReadDepth" FOLDED="true" ID="ID_164" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="VariantReadDepth" FOLDED="true" ID="ID_165" CREATED="1541758553126" MODIFIED="1541758553126">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="StrandBias" FOLDED="true" ID="ID_166" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicSourceClass" FOLDED="true" ID="ID_167" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="AllelicState" FOLDED="true" ID="ID_168" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
</node>
<node TEXT="Validation" FOLDED="true" ID="ID_169" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_170" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Method" FOLDED="true" ID="ID_171" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Status" FOLDED="true" ID="ID_172" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="CNV" FOLDED="true" ID="ID_173" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Alteration" FOLDED="true" ID="ID_174" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Chromosome" FOLDED="true" ID="ID_175" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStart" FOLDED="true" ID="ID_176" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomicStop" FOLDED="true" ID="ID_177" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GenomeBuild" FOLDED="true" ID="ID_178" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Cytoband" FOLDED="true" ID="ID_179" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="SegmentIntensity" FOLDED="true" ID="ID_180" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="SegmentGenomicStatus" FOLDED="true" ID="ID_181" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="CopyNumber" FOLDED="true" ID="ID_182" CREATED="1541758553127" MODIFIED="1541758553127">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="LOH" FOLDED="true" ID="ID_183" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Fusion" FOLDED="true" ID="ID_184" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_185" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Point5prime" FOLDED="true" ID="ID_186" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Point3prime" FOLDED="true" ID="ID_187" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="InFrame" FOLDED="true" ID="ID_188" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="NbSpanningPair" FOLDED="true" ID="ID_189" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="NbSplitReads" FOLDED="true" ID="ID_190" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="Expression" FOLDED="true" ID="ID_191" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="GenomeEntity" FOLDED="true" ID="ID_192" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
<node TEXT="Type" FOLDED="true" ID="ID_193" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Database" FOLDED="true" ID="ID_194" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Id" FOLDED="true" ID="ID_195" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="Symbol" FOLDED="true" ID="ID_196" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node TEXT="GeneDataType" FOLDED="true" ID="ID_197" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
<node TEXT="GeneValue" FOLDED="true" ID="ID_198" CREATED="1541758553128" MODIFIED="1541758553128">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
</node>
</node>
</map>
