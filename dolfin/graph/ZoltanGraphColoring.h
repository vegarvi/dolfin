// Copyright (C) 2010 Garth N. Wells.
// Licensed under the GNU LGPL Version 2.1.
//
// First added:  2010-11-16
// Last changed:

#ifndef __DOLFIN_ZOLTAN_GRAPH_COLORING_H
#define __DOLFIN_ZOLTAN_GRAPH_COLORING_H

#ifdef HAS_TRILINOS

#include <vector>
#include <boost/unordered_set.hpp>
#include <zoltan_cpp.h>
#include <dolfin/common/Array.h>
#include <dolfin/common/types.h>
#include "graph_types.h"

namespace dolfin
{

  class Mesh;

  /// This class colors a graph using Zoltan (part of Trilinos). It is designed
  /// to work on a single process.

  class ZoltanGraphColoring
  {

  public:

    /// Constructor
    ZoltanGraphColoring(const Graph& graph);

    /// Compute vertex colors
    void compute_local_vertex_coloring(Array<uint>& colors);

  private:

    /// Number of global graph vertices
    int num_global_vertices() const;

    /// Number of local graph vertices
    int num_local_vertices() const;

    /// Number of edges from each vertex
    void num_vertex_edges(uint* num_edges) const;

    // Graph
    const Graph graph;

    // Zoltan call-back functions
    static int get_number_of_objects(void* data, int* ierr);

    static void get_object_list(void* data, int sizeGID, int sizeLID,
                                ZOLTAN_ID_PTR globalID,
                                ZOLTAN_ID_PTR localID, int wgt_dim,
                                float* obj_wgts, int* ierr);

    static void get_number_edges(void* data, int num_gid_entries,
                                 int num_lid_entries,
                                 int num_obj, ZOLTAN_ID_PTR global_ids,
                                 ZOLTAN_ID_PTR local_ids, int* num_edges,
                                 int* ierr);

    static void get_all_edges(void* data, int num_gid_entries,
                              int num_lid_entries, int num_obj,
                              ZOLTAN_ID_PTR global_ids,
                              ZOLTAN_ID_PTR local_ids,
                              int* num_edges,
                              ZOLTAN_ID_PTR nbor_global_id,
                              int* nbor_procs, int wgt_dim,
                              float* ewgts, int* ierr);

  };

}

#endif
#endif