##Copyright 2008-2015 Thomas Paviot (tpaviot@gmail.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# OpenCASCADE Toolkits: each ToolKit is a list of modules
#
TOOLKIT_Foundation = {
            'TKernel': ['FSD', 'MMgt', 'OSD', 'Plugin', 'Quantity', 'Resource',
                        'SortTools',
                        'Standard', 'StdFail', 'Storage', 'TColStd',
                        'TCollection', 'TShort', 'Units', 'UnitsAPI',
                        'IncludeLibrary', 'Dico', 'NCollection', 'Message'],
            'TKMath': ['math', 'ElCLib', 'ElSLib', 'BSplCLib', 'BSplSLib',
                       'PLib', 'Precision', 'GeomAbs', 'Poly', 'CSLib',
                       'Convert', 'Bnd', 'gp', 'TColgp', 'TopLoc'],
            'TKAdvTools': ['Dynamic', 'Materials', 'Expr', 'ExprIntrp',
                           'GraphDS', 'GraphTools']}
TOOLKIT_Modeling = {
            'TKG2d': ['Geom2d', 'LProp', 'TColGeom2d', 'Adaptor2d',
                      'Geom2dLProp', 'Geom2dAdaptor', 'GProp'],
            'TKG3d': ['Geom', 'TColGeom', 'GeomAdaptor', 'AdvApprox',
                      'GeomLProp', 'Adaptor3d', 'LProp3d', 'TopAbs'],
            'TKGeomBase': ['ProjLib', 'GeomProjLib', 'GCPnts', 'CPnts',
                           'Approx', 'AppParCurves', 'FEmTool', 'AppCont',
                           'Extrema', 'IntAna', 'IntAna2d', 'GeomConvert',
                           'AdvApp2Var', 'GeomLib', 'Geom2dConvert', 'Hermit',
                           'BndLib', 'AppDef', 'GeomTools', 'GC', 'GCE2d',
                           'gce'],
            'TKBRep': ['TopoDS', 'TopExp', 'TopTools', 'BRep', 'BRepLProp',
                       'BRepAdaptor', 'BRepTools'],
            'TKGeomAlgo': ['Hatch', 'GeomInt', 'IntStart', 'IntWalk',
                           'IntImp', 'IntCurveSurface', 'IntSurf', 'IntPatch',
                           'Geom2dInt', 'IntImpParGen', 'IntRes2d', 'IntCurve',
                           'TopTrans', 'Intf', 'ApproxInt', 'TopTrans', 'Intf',
                           'ApproxInt', 'GccAna', 'GccEnt', 'GccInt', 'GccIter',
                           'GccGeo', 'HatchGen', 'Geom2dHatch', 'Law', 'TopTrans',
                           'Intf', 'ApproxInt', 'GccAna', 'GccEnt', 'GccInt',
                           'GccIter', 'GccGeo', 'HatchGen', 'Geom2dHatch',
                           'Law', 'AppBlend', 'Plate', 'GeomPlate',
                           'LocalAnalysis', 'GeomAPI', 'GeomFill', 'Geom2dAPI',
                           'Geom2dGcc', 'FairCurve', 'NLPlate', 'IntPolyh',
                           'TopClass'],
            'TKTopAlgo': ['IntCurvesFace', 'MAT', 'MAT2d', 'Bisector',
                          'BRepMAT2d', 'BRepCheck', 'BRepBndLib', 'BRepExtrema',
                          'BRepClass', 'BRepClass3d', 'BRepLib', 'BRepGProp',
                          'BRepIntCurveSurface', 'BRepTopAdaptor',
                          'BRepBuilderAPI', 'BRepApprox'],
            'TKPrim': ['BRepPrim', 'Primitives', 'BRepSweep', 'Sweep',
                       'BRepPrimAPI'],
            'TKBO': ['IntTools', 'BRepAlgoAPI', 'BOPCol', 'BOPInt', 'BOPDS',
                     'BOPAlgo', 'BOPTools'],
            'TKHLR': ['HLRTopoBRep', 'HLRBRep', 'HLRAlgo', 'HLRAppli',
                      'Intrv', 'TopBas', 'TopCnx', 'Contap'],
            'TKMesh': ['BRepMesh', 'IntPoly'],
            'TKShHealing': ['ShapeBuild', 'ShapeExtend', 'ShapeConstruct',
                            'ShapeCustom', 'ShapeAnalysis', 'ShapeFix',
                            'ShapeUpgrade', 'ShapeAlgo', 'ShapeProcess',
                            'ShapeProcessAPI'],
            'TKXMesh': ['XBRepMesh'],
            'TKBool': ['TopOpeBRep', 'TopOpeBRepDS', 'TopOpeBRepBuild',
                       'TopOpeBRepTool', 'BRepAlgo', 'BRepFill', 'BRepProj'],
            'TKFillet': ['ChFiDS', 'ChFi2d', 'ChFi3d', 'ChFiKPart', 'Blend',
                         'BRepBlend', 'BlendFunc', 'BRepFilletAPI',
                         'FilletSurf'],
            'TKFeat': ['LocOpe', 'BRepFeat'],
            'TKOffset': ['BRepOffsetAPI', 'Draft', 'BRepOffset', 'BiTgte'],
            }


TOOLKIT_Visualisation = {
            'TKService': ['Aspect', 'SelectBasics', 'Image',
                          'InterfaceGraphic', 'TColQuantity'],
            'TKV3d': ['V3d', 'Graphic3d', 'Visual3d', 'Select3D',
                      'Prs3d', 'StdPrs', 'SelectMgr', 'PrsMgr',
                      'AIS', 'DsgPrs', 'StdSelect'],
            'TKMeshVS': ['MeshVS'],
            }

TOOLKIT_DataExchange = {
            'TKSTL': ['StlMesh', 'StlAPI', 'StlTransfer', 'RWStl'],
            'TKSTEP': ['STEPControl'],
            'TKSTEPBase': ['StepBasic', 'RWStepBasic', 'StepRepr',
                           'RWStepRepr', 'StepGeom', 'RWStepGeom',
                           'StepShape', 'RWStepShape'],
            'TKIGES': ['IGESControl'],
            'TKXSBase': ['Interface', 'IFSelect'],
            }

TOOLKIT_OCAF = {
            'TKCAF': ['TDataXtd', 'TNaming', 'TPrsStd', 'AppStd'],
            'TKCDF': [],
            'PTKernel': [],
            'TKLCAF': ['TDF', 'TDataStd', 'TFunction', 'TDocStd', 'AppStdL'],
            'FWOSPlugin': [],
            'TKPShape': [],
            'TKBinL': [],
            'TKXmlL': [],
            'TKPLCAF': [],
            'TKTObj': [],
            'TKShapeSchema': [],
            'TKStdLSchema': [],
            'TKXCAF': ['XCAFApp', 'XCAFDoc', 'XCAFPrs'],
            'TKXDESTEP': ['STEPCAFControl'],
            'TKXDEIGES': ['IGESCAFControl'],
            }

TOOLKIT_SMesh = {
            'SMESH': ['SMDSAbs', 'SMDS', 'SMESH', 'SMESHDS', 'StdMeshers', 'NETGENPlugin']
            }

# List of modules to export
#
# (string module_name, list additional headers, list classes_to_exclude,
# dict member_functions to exclude)

OCE_MODULES = [
           ###
           ### FOUNDATION
           ###
           ###
           ### TKernel
           ('Dico', [], []),
           ('FSD', [], ['*']),
           ('MMgt', [], []),
           ('Message', [], ['Message_Msg']),
           ('NCollection', [], ['*']),
           ('OSD', [], ['*']),
           ('Plugin', [], ['*']),
           ('Quantity', [], []),
           ('Resource', [], ['*']),
           ('SortTools', [], []),
           ('Standard', [], ['Standard_AncestorIterator',
                             'Standard_Persistent', 'Standard_Static_Assert',
                             'Standard_CLocaleSentry'],
            {'Standard_MMgrOpt': 'SetCallBackFunction',
             'Standard': 'Free',
             'Standard_Failure': ['operator=', 'Raise', 'Reraise'],
             'Standard_ErrorHandlerCallback': ['RegisterCallback','UnregisterCallback']}),
           ('StdFail', [], ['*']),
           ('Storage', [], ['Storage_Bucket', 'Storage_BucketIterator',
                            'Storage_BucketOfPersistent']),
           ('TColStd', [], ['TColStd_PackedMapOfInteger']),
           ('TCollection', [], []),
           ('TShort', [], []),
           ('Units', [], ['Units_Quantity', 'Units_Dimensions']),
           ('UnitsAPI', [], []),
           ('IncludeLibrary', [], ['*']),
           ### TKMath
           ('math', [], ['*']),
           ('ElCLib', [], []),
           ('ElSLib', [], []),
           ('BSplCLib', [], ['BSplCLib_EvaluatorFunction'], {'BSplCLib': ['DN']}),
           ('BSplSLib', [], ['BSplSLib_EvaluatorFunction']),
           ('PLib', [], []),
           ('Precision', [], []),
           ('GeomAbs', [], []),
           ('Poly', ['NCollection'],
            ['Poly_CoherentTriPtr', 'Poly_CoherentTriangulation',
             'Poly_MakeLoops', 'Poly_MakeLoops3D', 'Poly_MakeLoops2D']),
           ('CSLib', [], []),
           ('Convert', [], []),
           ('Bnd', [], []),
           ('gp', [], [],
            {'gp_Torus': 'Coefficients'}),
           ('TColgp', [], []),
           ('TopLoc', [], [],
            {'TopLoc_SListNodeOfSListOfItemLocation': 'Count'}),
           ### TKAdvTools
           ('Dynamic', [], []),
           ('Materials', [], []),
           ('Expr', [], ['Expr_Sign']),
           ('ExprIntrp', [], []),
           ('GraphDS', [], []),
           ('GraphTools', [], []),
           ###
           ### MODELING DATA
           ###
           ###
           ### TKG2d
           ('Geom2d', [], []),
           ('LProp', [], []),
           ('TColGeom2d', [], []),
           ('Adaptor2d', [], []),
           ('Geom2dLProp', [], []),
           ('Geom2dAdaptor', [], []),
           ('GProp', [], []),
           ### TKG3d
           ('Geom', [], []),
           ('TColGeom', [], []),
           ('GeomAdaptor', ['Geom2d'], []),
           ('AdvApprox', [], ['AdvApprox_EvaluatorFunction']),
           ('GeomLProp', [], []),
           ('Adaptor3d', [], []),
           ('LProp3d', [], []),
           ('TopAbs', [], []),
           ### TKGeomBase
           ('ProjLib', [], [],
            {'ProjLib_ProjectOnSurface': 'Load',
             'ProjLib_ProjectedCurve': 'Load'}),
           ('GeomProjLib', [], []),
           ('GCPnts', [], []),
           ('CPnts', [], []),
           ('Approx', ['FEmTool'], []),
           ('AppParCurves', [], ['*']),
           ('FEmTool', [], []),
           ('AppCont', [], []),
           ('Extrema', [], []),
           ('IntAna', [], []),
           ('IntAna2d', [], []),
           ('GeomConvert', [], [],
            {'GeomConvert_CompCurveToBSplineCurve': 'Clear'}),
           ('AdvApp2Var', [], ['AdvApp2Var_EvaluatorFunc2Var',
                               'AdvApp2Var_Iso']),
           ('GeomLib', [], []),
           ('Geom2dConvert', [], []),
           ('Hermit', [], []),
           ('BndLib', [], []),
           ('AppDef', [], ['*']),
           ('GeomTools', ['Handle_TCollection', 'TColStd', 'TColgp'], []),
           ('GC', [], []),
           ('GCE2d', [], []),
           ('gce', [], []),
           ### TKBRep
           ('TopoDS', [], []),
           ('TopExp', ['Message', 'TopLoc'], []),
           ('TopTools', [], []),
           ('BRep', ['TShort'], []),
           ('BRepLProp', [], []),
           ('BRepAdaptor', ['TopLoc', 'Geom2d'], []),
           ('BRepTools', ['TShort', 'Poly'], []),
           ### TKGeomAlgo
           ('Hatch', [], []),
           ('GeomInt', [], ['*']),
           ('IntStart', [], []),
           ('IntWalk', [], ['*']),
           ('IntImp', [], []),
           ('IntCurveSurface', ['Geom2d'],
            ['IntCurveSurface_ThePolyhedronOfHInter']),
           ('IntSurf', [], []),
           ('IntPatch', [], ['*']),
           ('Geom2dInt', ['Adaptor3d', 'Geom', 'Geom2d'], [],
            {'Geom2dInt_Geom2dCurveTool': 'IsComposite',
             'Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter': 'Locate'}),
           ('IntImpParGen', [], ['IntImpParGen_ImpTool']),
           ('IntRes2d', [], []),
           ('IntCurve', ['Geom2d'], []),
           ('TopTrans', [], []),
           ('Intf', [], []),
           ('ApproxInt', [], []),
           ('GccAna', [], []),
           ('GccEnt', [], []),
           ('GccInt', [], []),
           ('GccIter', [], []),
           ('GccGeo', [], []),
           ('HatchGen', [], []),
           ('Geom2dHatch', ['Adaptor3d', 'Geom2d',
                            'Intf', 'Extrema', 'Bnd', 'Geom'], [],
            {'Geom2dHatch_Hatcher': 'IsDone'}),
           ('Law', ['Geom', 'Geom2d'], [],
            {'Law_Interpolate': 'ClearTangents'}),
           ('AppBlend', [], []),
           ('Plate', [], []),
           ('GeomPlate', ['PLib'], []),
           ('LocalAnalysis', [], []),
           ('GeomAPI', [], [],
            {'GeomAPI_Interpolate': 'ClearTangents'}),
           ('GeomFill', ['FEmTool', 'AppParCurves', 'PLib'],
            ['GeomFill_NSections',
             'GeomFill_SweepSectionGenerator'],
            {'GeomFill_FunctionGuide': 'Deriv2T'}),
           ('Geom2dAPI', [], [],
            {'Geom2dAPI_Interpolate': 'ClearTangents'}),
           ('Geom2dGcc', [], ['Geom2dGcc_FuncTCuCuCuOfMyC2d3Tan'],
            {'Geom2dGcc_Lin2dTanObl': 'IsParallel2'}),
           ('FairCurve', [], []),
           ('NLPlate', [], []),
           ('IntPolyh', ['Geom', 'Geom2d'], ['IntPolyh_Array',
                                             'IntPolyh_MaillageAffinage'],
            {'IntPolyh_Triangle': 'GetNextChainTriangle'}),
           ('TopClass', [], []),
           ### TKTopALgo
           ('IntCurvesFace', [], []),
           ('MAT', [], []),
           ('MAT2d', [], ['MAT2d_SketchExplorer', 'MAT2d_CutCurve']),
           ('Bisector', [], []),
           ('BRepMAT2d', ['TopLoc'], []),
           ('BRepCheck', ['TopLoc', 'Message'], []),
           ('BRepBndLib', [], []),
           ('BRepExtrema', [], []),
           ('BRepClass', [], ['BRepClass_FaceClassifier']),
           ('BRepClass3d', ['TopLoc', 'GeomAdaptor', 'IntSurf',
                            'Adaptor3d', 'Geom', 'Geom2d', 'Adaptor2d',
                            'Geom2dAdaptor'], []),
           ('BRepLib', [], []),
           ('BRepGProp', [], [],
            {'BRepGProp_VinertGK': 'GetAbsolutError'}),
           ('BRepIntCurveSurface', [], []),
           ('BRepTopAdaptor', ['Geom', 'Geom2d', 'GeomAdaptor',
                               'TopLoc', 'Geom2dAdaptor'], []),
           ('BRepBuilderAPI', ['BRep', 'TopLoc', 'TShort', 'Poly'], [],
            {'BRepBuilderAPI_VertexInspector': 'Inspect'}),
           ('BRepApprox', ['TopLoc', 'TopoDS', 'FEmTool', 'GeomAdaptor',
                           'Geom2dAdaptor'], [],
            {'BRepApprox_ResConstraintOfMyGradientbisOfTheComputeLineOfApprox': 'Error',
             'BRepApprox_ResConstraintOfMyGradientOfTheComputeLineBezierOfApprox': 'Error',
             'BRepApprox_Approx': 'Perform'}),
           ### TKPrim
           ('BRepPrim', [], []),
           ('Primitives', [], []),
           ('BRepSweep', ['Geom', 'Geom2d', 'TShort', 'Poly'], []),
           ('Sweep', [], []),
           ('BRepPrimAPI', [], []),
           ### TKBO
           ('IntTools', ['AppParCurves', 'IntRes2d', 'Geom2dInt',
                         'Adaptor3d', 'FEmTool', 'Extrema', 'IntAna',
                         'Intf', 'IntSurf', 'BRepAdaptor', 'Quantity',
                         'HatchGen', 'TopLoc', 'Approx', 'BRepClass3d',
                         'IntCurveSurface', 'Geom2dHatch', 'GeomAdaptor',
                         'Geom2dAdaptor'],
                        ['IntTools_CArray1OfInteger',
                         'IntTools_CArray1OfReal'],
            {'IntTools_PntOnFace': 'IsValid'}),
           ('BRepAlgoAPI', [], []),
           ('BOPCol', [], ['*']),
           ('BOPInt', ['AppParCurves', 'Handle_IntPatch',
                       'Adaptor3d', 'FEmTool', 'Extrema', 'IntAna',
                       'Intf', 'IntSurf', 'BRepAdaptor', 'Quantity',
                       'HatchGen', 'TopLoc', 'Approx', 'Geom2d',
                       'Geom2dInt', 'GeomAdaptor', 'Geom2dAdaptor'], []),
           ('BOPDS', ['IntTools','AppParCurves',
                      'Adaptor3d', 'FEmTool', 'Extrema', 'IntAna',
                      'Intf', 'IntSurf', 'BRepAdaptor', 'Quantity',
                      'HatchGen', 'TopLoc', 'Approx', 'Geom2dHatch',
                      'IntRes2d', 'Geom', 'Geom2d', 'BRepClass3d',
                      'IntCurveSurface', 'GeomAdaptor', 'Geom2dInt',
                      'Geom2dAdaptor'], ['BOPDS_Interf'],
            {'BOPDS_CoupleOfPaveBlocks': 'Handle'}),
           ('BOPAlgo', [], ['*']),
           ('BOPTools', [], [],
            {'BOPTools_AlgoTools2D': 'MakeCurveOnSurface'}),
           ### TKHLR
           ('HLRTopoBRep', ['TColStd', 'TColgp', 'BRepAdaptor',
                            'TopLoc', 'IntSurf', 'GeomAdaptor', 'Geom',
                            'Adaptor3d', 'Message', 'Geom2dAdaptor'], []),
           ('HLRBRep', ['Message', 'Contap', 'GeomAdaptor', 'TopLoc',
                        'Geom2dAdaptor'],
            ['HLRBRep_ThePolyhedronOfInterCSurf', 'HLRBRep_BSurfaceTool',
             'HLRBRep_Surface',
             'HLRBRep_TheCurveLocatorOfTheProjPCurOfCInter']),
           ('HLRAlgo', [], []),
           ('HLRAppli', [], []),
           ('Intrv', [], []),
           ('TopBas', [], []),
           ('TopCnx', [], []),
           ('Contap', ['TColgp', 'Geom'], []),
           ### TKMesh
           ('BRepMesh', ['TShort', 'Adaptor3d', 'Geom2dAdaptor', 'Message',
                         'Adaptor2d', 'GeomAdaptor', 'Geom', 'TopLoc',
                         'Geom2d'],
            ['BRepMesh_DiscretFactory'],
            {'BRepMesh_CircleInspector': ['BRepMesh_CircleInspector', 'Inspect'],
             'BRepMesh_Delaun': ['Frontier', 'InternalEdges', 'FreeEdges'],
             'BRepMesh_VertexInspector': ['BRepMesh_VertexInspector', 'Add', 'Inspect']}),
           ('IntPoly', ['TColStd', 'TopLoc'], []),
           ### TKShHealing
           ('ShapeBuild', ['TShort', 'TColGeom', 'BRep', 'Message',
                           'TopTools', 'Bnd', 'TCollection',
                           'Poly'], []),
           ('ShapeExtend', ['TColgp', 'TopLoc', 'Poly', 'IntRes2d',
                            'BRepBuilderAPI', 'GeomAdaptor'], []),
           ('ShapeConstruct', ['TCollection', 'BRep', 'Bnd', 'Adaptor2d',
                               'TColGeom', 'Adaptor3d', 'TopLoc',
                               'TShort', 'Message', 'Poly', 'BRepTools',
                               'IntRes2d', 'BRepBuilderAPI', 'GeomAdaptor'], []),
           ('ShapeCustom', ['BRep', 'Message', 'Poly', 'TShort',
                            'Bnd'],
            ['ShapeCustom_BSplineRestriction',
             'ShapeCustom_SweptToElementary',
             'ShapeCustom_ConvertToRevolution']),
           ('ShapeAnalysis', ['TColGeom', 'Message'],
            ['ShapeAnalysis_BoxBndTreeSelector']),
           ('ShapeFix', ['TColGeom', 'BRep', 'TShort',
                         'Adaptor3d', 'Poly', 'BRepTools',
                         'IntRes2d', 'BRepBuilderAPI', 'GeomAdaptor'],
            ['ShapeFix_WireSegment']),
           ('ShapeUpgrade', ['BRep', 'Bnd', 'TShort', 'Adaptor3d',
                             'TCollection', 'Message', 'Poly','BRepTools',
                             'IntRes2d', 'BRepBuilderAPI', 'GeomAdaptor'], []),
           ('ShapeAlgo', ['Geom', 'TopTools', 'BRep', 'TColGeom', 'TopLoc',
                          'Message', 'Bnd', 'Geom2d', 'ShapeAnalysis',
                          'TShort', 'ShapeExtend', 'Adaptor3d',
                          'Poly', 'TopoDS', 'BRepTools', 'IntRes2d',
                          'BRepBuilderAPI', 'GeomAdaptor'],
            ['ShapeAlgo_AlgoContainer']),
           ('ShapeProcess', ['BRep', 'TShort', 'TColGeom', 'Poly',
                             'Bnd', 'Geom2d', 'Geom', 'TopLoc'], []),
           ('ShapeProcessAPI', [], []),
           ### TKXMesh
           ('XBRepMesh', [], []),
           ### TKBool
           ('TopOpeBRep', ['TColStd', 'TCollection', 'TopLoc', 'TColgp',
                           'Adaptor3d', 'IntAna', 'Message', 'IntSurf',
                           'Extrema','IntCurveSurface', 'Geom2d', 'Geom2dAdaptor',
                           'BRepAdaptor', 'GeomAdaptor'],
            ['TopOpeBRep_traceSIFF'],
            {'TopOpeBRep_FacesFiller': 'EqualpP',
             'TopOpeBRep_EdgesIntersector': 'Tolerance2',
             'TopOpeBRep_GeomTool': 'MakePrivateCurves'}),
           ('TopOpeBRepDS', ['TopLoc', 'TColgp', 'Adaptor2d', 'Bnd',
                             'BRepAdaptor', 'Adaptor3d', 'Intf',
                             'Message', 'IntSurf', 'Extrema',
                             'IntCurveSurface', 'Geom2d', 'Geom2dAdaptor',
                             'BRepAdaptor', 'GeomAdaptor'],
            ['TopOpeBRepDS_DSS', 'TopOpeBRepDS_HDataStructure'],
            {'TopOpeBRepDS_Dumper': 'Print'}),
           ('TopOpeBRepBuild', ['Geom', 'Adaptor2d', 'Bnd',
                                'BRepAdaptor', 'TopLoc', 'Adaptor3d',
                                'Message', 'Intf', 'IntSurf', 'Extrema',
                                'IntCurveSurface', 'Geom2d', 'Geom2dAdaptor',
                                'BRepAdaptor', 'GeomAdaptor'], [],
            {'TopOpeBRepBuild_Builder1': 'GFillSplitsPVS'}),
           ('TopOpeBRepTool', ['Geom', 'Adaptor2d', 'Bnd',
                               'BRepAdaptor', 'TopLoc', 'Adaptor3d',
                               'Message', 'Intf', 'IntSurf', 'Extrema',
                               'IntCurveSurface', 'Geom2d', 'Geom2dAdaptor',
                               'BRepAdaptor', 'GeomAdaptor'],
            ['TopOpeBRepTool_STATE', 'TopOpeBRepTool_mkTondgE']),
           ('BRepAlgo', ['TopExp', 'TopLoc', 'IntSurf', 'BRep',
                         'TopOpeBRepDS', 'Bnd', 'Message',
                         'TShort', 'Intf', 'TopOpeBRepTool',
                         'Poly', 'Extrema', 'BRepTools', 'IntCurveSurface',
                         'Geom2d', 'Geom2dAdaptor', 'BRepAdaptor',
                         'GeomAdaptor'], [],
            {'BRepAlgo_DSAccess': 'IsDeleted'}),
           ('BRepFill', ['FEmTool', 'TColGeom2d', 'PLib', 'TopLoc',
                         'Plate', 'AdvApp2Var', 'TColGeom',
                         'Message', 'Convert', 'Approx'], []),
           ('BRepProj', [], []),
           ### TKFillet
           ('ChFiDS', ['Message', 'TopLoc', 'GeomAdaptor',
                       'Geom2dAdaptor', 'IntCurveSurface'], []),
           ('ChFi2d', [], []),
           ('ChFi3d', [], []),
           ('ChFiKPart', ['TopTools', 'TColStd', 'TColgp',
                          'BRepAdaptor', 'Geom', 'Bnd', 'BRepClass3d',
                          'TopoDS', 'gp', 'TopLoc', 'Message',
                          'Intf', 'IntSurf', 'TopOpeBRepTool',
                          'Law', 'Extrema', 'IntCurveSurface',
                          'Geom2dAdaptor'], []),
           ('Blend', ['Geom2d'], []),
           ('BRepBlend', ['AppParCurves', 'TCollection', 'PLib', 'FEmTool',
                          'Convert', ], []),
           ('BlendFunc', [], ['*']),
           ('BRepFilletAPI', [], []),
           ('FilletSurf', ['TopoDS'], []),
           ### TKFeat
           ('LocOpe', ['TColStd', 'Bnd', 'BRepAdaptor',
                       'BRepClass3d', 'Adaptor3d', 'TopLoc',
                       'Intf', 'Message', 'IntSurf',
                       'TopOpeBRepTool', 'Extrema', 'Geom2d',
                       'IntCurveSurface', 'GeomAdaptor', 'Geom2dAdaptor'],
            ['LocOpe_Revol', 'LocOpe_RevolutionForm']),
           ('BRepFeat', ['TopLoc', 'BRepAdaptor', 'Adaptor3d'], [],
            {'BRepFeat': 'IsInOut',
             'BRepFeat_MakeLinearForm': 'TransformShapeFU'}),
           ### TKOffset
           ('BRepOffsetAPI', ['Bnd', 'AppParCurves', 'MAT', 'TColgp',
                              'BRepAlgo', 'FEmTool', 'TopOpeBRepBuild',
                              'Plate', 'Bisector', 'TColStd', 'PLib',
                              'BRepMAT2d', 'TColGeom2d', 'BRepAdaptor',
                              'BRepClass3d', 'BRep', 'BRepTools',
                              'Quantity', 'Adaptor3d', 'TopLoc',
                              'AdvApp2Var', 'TColGeom', 'IntSurf',
                              'Message', 'Convert', 'Intf', 'TShort',
                              'TopOpeBRepDS', 'Poly', 'TopOpeBRepTool',
                              'Extrema', 'Geom2d', 'IntCurveSurface',
                              'GeomAdaptor', 'Geom2dAdaptor',
                              'BRepBuilderAPI', 'GeomPlate'], [],
            {'BRepOffsetAPI_FindContigousEdges': 'NbEdges'}),
           ('BRepOffset', ['Quantity', 'Bnd', 'AppParCurves', 'MAT', 'TColgp',
                           'BRepAlgo', 'FEmTool', 'TopOpeBRepBuild',
                           'Plate', 'Bisector', 'TColStd',
                           'BRepMAT2d', 'TColGeom2d', 'BRepAdaptor',
                           'BRepClass3d', 'BRep', 'BRepTools',
                           'Quantity', 'Adaptor3d', 'TopLoc',
                           'AdvApp2Var', 'TColGeom', 'IntSurf',
                           'Message', 'Convert', 'Intf', 'TShort',
                           'TopOpeBRepDS', 'Poly', 'TopOpeBRepTool',
                           'Extrema', 'Geom2d', 'IntCurveSurface',
                           'GeomAdaptor', 'Geom2dAdaptor',
                           'BRepBuilderAPI'], [],
            {'BRepOffset_MakeOffset': 'GetAnalyse'}),
           ('Draft', ['BRep', 'Bnd', 'TShort', 'Message',
                      'Poly'], []),
           ('BiTgte', ['TopLoc', 'Message'], []),
           ###
           ### Visualisation
           ###
           ###
           ### TKService
           ('Aspect', [], ['Aspect_DisplayConnection']),
           ('SelectBasics', [], []),
           ('Image', [], ['*']),
           ('InterfaceGraphic', [], []),
           ('TColQuantity', [], []),
           ### TKV3d
           ('V3d', ['TShort', 'TColQuantity'], [],
            {'V3d_Viewer': 'Print', 'V3d_View': 'Print'}),
           ('Graphic3d', ['TShort', 'TColQuantity'],
            ['Graphic3d_UniformValue', 'Graphic3d_UniformValueType',
             'Graphic3d_ClipPlane', 'Graphic3d_UniformValueTypeID'],
            {'Graphic3d_ShaderVariable': 'Create',
             'Graphic3d_ValueInterface': 'As',
             'Graphic3d_ShaderProgram': 'PushVariable',
             'Graphic3d_AspectText3d': 'Values',
             'Graphic3d_Group': 'SetGroupPrimitivesAspect',
             'Graphic3d_GraphicDriver': 'Print'}),
           ('Visual3d', ['TShort', 'TColQuantity'], [],
            {'Visual3d_View': 'Print',
             'Visual3d_Layer': 'DrawText'}),
           ('Select3D', ['TShort', 'TColQuantity', 'Aspect', 'Visual3d',
                         'Graphic3d', 'Quantity', 'Message'],
            ['Select3D_SensitiveTriangulation']),
           ('Prs3d', ['TShort', 'TColQuantity', 'Message'],
            ['Prs3d_WFShape', 'Prs3d_Point']),
           ('StdPrs', [], ['*']),
           ('SelectMgr', [], ['*']),
           ('PrsMgr', ['HLRAlgo', 'TopoDS', 'Aspect',
                       'Visual3d', 'TShort', 'Message',
                       'Bnd', 'TopTools', 'TColQuantity',
                       'Poly'], []),
           ('AIS', ['TopTools', 'Message', 'TShort', 'SelectBasics',
                    'Visual3d', 'HLRAlgo', 'TColQuantity'], [],
            {'AIS_LocalContext': 'Reactivate',
             'AIS_TexturedShape': 'ShowTriangles'}),
           ('DsgPrs', [], ['*']),
           ('StdSelect', [], ['*']),
           # MeshVS
           ('MeshVS', ['TopTools', 'Message', 'TShort',
                       'Geom', 'Visual3d', 'HLRAlgo', 'Poly',
                       'TColQuantity', 'TopoDS', 'V3d'], []),
           ###
           ### DataExchange
           ###
           ('StlMesh', [], []),
           ('StlAPI', [], []),
           ('StlTransfer', [], []),
           ('RWStl', [], []),
           ### TKSTEPBase
           ('StepBasic', ['MoniTool','TCollection','Handle_Interface','StepBasic',
                          'Message'], []),
           ('RWStepBasic', ['MoniTool','TCollection','Handle_Interface','StepBasic'], []),
           ('StepRepr', ['MoniTool','TCollection','Interface','StepBasic',
                         'Message'], []),
           ('RWStepRepr', ['MoniTool','TCollection','Handle_Interface','StepBasic'], []),
           ('StepGeom', ['MoniTool','TCollection','Handle_Interface','StepBasic',
                         'Message'], []),
           ('RWStepGeom', ['MoniTool','TCollection','Handle_Interface','StepBasic'], []),
           ('StepShape', ['MoniTool','TCollection','Handle_Interface','StepBasic',
                          'Message'], []),
           ('RWStepShape', ['MoniTool','TCollection','Handle_Interface','StepBasic'], []),
           ### TKSTEP
           ('STEPControl', ['Message', 'TopLoc', 'Dico'], []),
           ('IGESControl', ['Message', 'TopLoc', 'Dico', 'TopTools'], []),
           ('Interface', [], []),
           ('IFSelect', [], [], {'IFSelect_EditForm': 'NbTouched',
                                 'IFSelect_IntParam': 'StaticName',
                                 'IFSelect_ContextModif': 'Search'}),
           ('XSControl', ['Message', 'TopLoc', 'Dico'], []),
           ###
           ### OCAF
           ###
           ### TKLCAF
           ('TDF', [], ['TDF_LabelNode']),
           ('TDataStd', [], []),
           ('TFunction', [], []),
           ('TDocStd', [], []),
           ('AppStdL', ['TDF'], []),
           ### TKXCAF
           ('XCAFApp', ['TDF'], []),
           ('XCAFDoc', ['TDF', 'Message'], []),
           ('XCAFPrs', ['TopTools', 'Message', 'TShort', 'Poly', 'Aspect',
                        'V3d', 'Select3D', 'Geom', 'HLRAlgo', 'Bnd',
                        'SelectBasics', 'Visual3d', 'Prs3d',
                        'TColQuantity', 'TDF', 'TDataStd', 'TNaming',
                        'TDataXtd'], []),
           ### TKCAF
           ('TDataXtd',  ['TopTools', 'TCollection', 'Message', 'TopLoc'], []),
           ('TNaming',  ['TCollection', 'Message'], []),
           ('TPrsStd',  ['TDF', 'HLRAlgo', 'TopTools', 'TCollection', 'Geom',
                         'TDataStd', 'Aspect', 'Visual3d', 'TNaming', 'Select3D',
                         'TColQuantity', 'Message', 'Poly', 'Prs3d', 'Bnd',
                         'TopLoc', 'TShort', 'SelectBasics', 'TopoDS'], []),
           ('AppStd', ['TDF'], []),
           ### TKXDESTEP
           ('STEPCAFControl', ['Interface', 'TopLoc', 'TopTools',
                               'Message', 'Dico', 'Quantity'], []),
           ### TKXDEIGES
           ('IGESCAFControl', [], []),
           ]

SMESH_MODULES = [
           ('SMDSAbs', [], []),
           ('SMDS', [], ['SMDS_EXPORT', 'SMDS_Iterator'],
             {'SMDS_Mesh': ['ChangeElementNodes', 'boundaryEdges', 'boundaryFaces'],
              'SMDS_FaceOfNodes': 'ChangeNodes',
              'SMDS_PolygonalFaceOfNodes': 'ChangeNodes',
              'SMDS_QuadraticFaceOfNodes': 'ChangeNodes',
              'SMDS_QuadraticVolumeOfNodes': 'ChangeNodes',
              'SMDS_VolumeOfNodes': 'ChangeNodes',
              'SMDS_SpacePosition': ['SetCoords', 'GetTypeOfPosition']}),
           ('SMESHDS', [], ['SMESHDS_GroupBase', 'SMESHDS_Hypothesis'],
            {'SMESHDS_Mesh': 'ChangeElementNodes', 'SMESHDS_Command': 'ChangeElementNodes',
             'SMESHDS_Script': 'ChangeElementNodes'}),
           ('SMESH', ['math', 'gp', 'TopExp', 'TColStd', 'TShort',
                      'Message', 'TCollection', 'Graphic3d', 'AIS', 'Aspect',
                      'HLRAlgo', 'Poly', 'V3d', 'Select3D', 'Geom', 'TopTools',
                      'SelectBasics', 'Visual3d', 'Prs3d', 'Quantity',
                      'TColQuantity', 'TopLoc', 'Bnd'],
                     ['SMESH_Comment', 'SMESH_Octree',
                      'SMESH_Array1', 'SMESH_Array2',
                      'SMESH_MeshEditor'],
            {'SMESH_Hypothesis': 'IsStatusFatal', 'SMESH_Mesh': 'GetGroups',
             'SMESH_MesherHelper': 'IsQuadraticMesh'},),
           ('StdMeshers', ['TopTools', 'Adaptor3d'], ['StdMeshers_CompositeSegment_1D'],
            {'StdMeshers_Arithmetic1D': 'SetParametersByDefaults',
             'StdMeshers_CompositeHexa_3D': 'CheckHypothesis',
             'StdMeshers_Hexa_3D': 'OppositeVertex',
             'StdMeshers_NumberOfSegments': 'SetDistrType',
             'StdMeshers_ProjectionUtils': 'FindFaceAssociation'
             }),
           ('NETGENPlugin', [], [],
            {'NETGENPlugin_NETGEN_2D': 'CheckHypothesis',
            'NETGENPlugin_NETGEN_2D3D': 'CheckHypothesis',
            'NETGENPlugin_NETGEN_3D': 'CheckHypothesis',
            'NETGENPlugin_NETGEN_2D_ONLY': 'CheckHypothesis'}),
           ]

if __name__ == '__main__':
    print(get_wrapped_modules_names())
